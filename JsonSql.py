import copy


class JsonSql:
    def _insert(self, table, type, name, value):
        text = ""
        text += " INSERT INTO "
        text += table
        text += " VALUES('" + type + "','" + name + "','" + value + "')\n "
        return text

    def _create(self, table):
        text = ""
        text += " CREATE TABLE "
        text += table
        text += " (Type VARCHAR(10), Name VARCHAR(100), Value NVARCHAR(250))\n "
        return text

    def getSql(self, ser, sch, table, project_name):
        ser = copy.deepcopy(ser)
        sch = copy.deepcopy(sch)
        request = ""
        for i in range(len(sch.keys())):
            var = list(sch.keys())[i]
            # project_name + '_' +
            schema = sch[var]
            if (schema['type'] == 'array'):
                type = schema['items']['type']
                new_table = project_name + '_' + var
                r = self._insert(table, schema['type'], var, new_table)
                rr = self._create(new_table)
                request += r
                request += rr

                if (type == 'object'):
                    for j in range(len(ser[var])):
                        r = self._insert(new_table, schema['items']['type'], var, new_table + str(j))
                        new_table += str(j)
                        rr = self._create(new_table)
                        request += rr
                        request += r
                        request += self.getSql(ser[var][j], schema['items']['properties'], new_table, project_name)
                elif (type == 'array'):
                    for j in range(len(ser[var])):
                        r = self._insert(new_table, schema['items']['type'], var, new_table + str(j))
                        new_table += str(j)
                        rr = self._create(new_table)
                        request += rr
                        request += r
                        request += self.getSql(ser[j], schema[var], new_table, project_name)
                else:
                    for j in range(len(ser[var])):
                        pass
                        #s += str(ser[var][j])
            elif (schema['type'] == 'object'):
                new_table = project_name + '_' + var
                r = self._insert(table, schema['type'], var, new_table)
                rr = self._create(new_table)
                request += r
                request += rr
                request += self.getSql(ser[var], schema['properties'], new_table, project_name)
            else:
                r = self._insert(table, schema['type'], var, str(ser[var]))
                request += r
        return request

    def _replace(self, string, table):
        return string.replace(string, table + '_', '')

    def _unpack(self, cursor, table):
        def _unpack_array(cursor, table):
            cursor.execute("SELECT * FROM " + table)
            json = ""
            first = True
            db = cursor.fetchall()
            for elem in db:
                type = elem[0]
                variable = elem[1]
                value = elem[2]
                if (not first):
                    json += ','
                if (type == "object"):

                    first = False
                    json += "{\n"
                    json += self._unpack(cursor, value)
                    json += "\n}\n"
                elif (type == "array"):
                    "[\n"
                    json += _unpack_array(cursor, value)
                    json += "\n]\n"
                elif (type == "string"):
                    json += '"' + value + '"'
                    first = False
                else:
                    json += str(value)
                    first = False
            return json

        cursor.execute("SELECT * FROM " + table)
        json = ""
        db = cursor.fetchall()
        first = True
        for elem in db:
            type = elem[0]
            variable = elem[1]
            value = elem[2]
            if (not first):
                json += ',\n'
            if (type == "object"):
                first = False
                json += '"' + variable + '": '
                json += "{\n"
                json += self._unpack(cursor, value)
                json += "\n}\n"

            elif (type == "array"):
                json += '"' + variable + '": [\n'
                json += _unpack_array(cursor, value)
                json += "\n]\n"
            elif (type == "string"):
                json += '"' + variable + '": ' + '"' + value + '"'
                first = False
            else:
                json += '"' + variable + '": ' + str(value) + ''
                first = False

        return json

    def unpack(self, cursor, table):
        return '{\n' + self._unpack(cursor, table) + '\n}'




