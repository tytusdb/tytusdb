```bnf
<start> ::= <sentences> { start.val = sentences.val }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<dml> ::= <truncate> { dml.val = truncate.val }
<truncate> ::= TRUNCATE TABLE <idList> { truncate.val = Truncate(idList.val,) }
<idList> ::= <idList> ',' ID { ID.val='TABLE2'; idList.val = idList1.val.append(ID.val) }
<idList> ::= ID { ID.val='TABLE1'; idList.val = [ID.val] }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<dml> ::= <delete> { dml.val = delete.val }
<delete> ::= DELETE FROM ID WHERE <expression> { ID.val='DELETE'; delete.val = Delete(ID.val,expression.val) }
<expression> ::= <expression> = <expression> { expression.val = Relational(expression1.val,expression2.val,'=') }
<expression> ::= <expression> + <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'+') }
<expression> ::= INT { INT.val=int(1); expression.val = INT.val  }
<expression> ::= INT { INT.val=int(1); expression.val = INT.val  }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<dml> ::= <update> { dml.val = update.val }
<update> ::= UPDATE ID SET <reallocationOfValues> WHERE <expression> { ID.val='CASAS'; update.val=Update(ID.val,reallocationOfValues.val,expression.val) }
<expression> ::= <expression> = <expression> { expression.val = Relational(expression1.val,expression2.val,'=') }
<expression> ::= INT { INT.val=int(1); expression.val = INT.val  }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<reallocationOfValues> ::= <reallocationOfValues> ',' ID '=' <expression> { ID.val='FECHA'; reallocationOfValues.val = reallocationOfValues1.val.append([ID.val,expression.val]) }
<expression> ::= REGEX { REGEX.val=val('2019/09/07'); expression.val = REGEX.val  }
<reallocationOfValues> ::= <reallocationOfValues> ',' ID '=' <expression> { ID.val='CLAVE'; reallocationOfValues.val = reallocationOfValues1.val.append([ID.val,expression.val]) }
<expression> ::= INT { INT.val=int(1234); expression.val = INT.val  }
<reallocationOfValues> ::= ID '=' <expression> { ID.val='GRUPO'; reallocationOfValues.val = [ID.val,expression.val] }
<expression> ::= REGEX { REGEX.val=val('NUEVO'); expression.val = REGEX.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <ddl> ';' { sentence.val = ddl.val }
<ddl> ::= <create> { ddl.val = create.val }
<create> ::= <createTable> { create.val = createTable.val }
<createTable> ::=  CREATE TABLE ID '(' <columns> ')' INHERITS '(' ID ')' { ID1.val='CASAS'; ID1.val='USUARIOS'; createTable.val = CreateTable(ID1.val,columns.val,ID2.val); }
<columns> ::= <columns> ',' <column> { columns.val = columns.val.append(column.val) }
<column> ::= PRIMARY KEY '(' <idList> ')' { column.val = ColumnPrimaryKey(idList.val) }
<idList> ::= ID { ID.val='ID'; idList.val = [ID.val] }
<columns> ::= <columns> ',' <column> { columns.val = columns.val.append(column.val) }
<column> ::= ID <type> <opt1> { ID.val='FECHA'; column.val = ColumnId(ID.val, type.val, opt1.val) }
<opt1> ::= <null> { opt1.val = null.val }
<null> ::= NULL (<default>|<primarys>|<reference>|<uniques>|<checks>) { null.val={'null':True} + option.val }
<checks> ::= CHECK '(' <expression> ')' { checks.val={'check':expression.val} }
<expression> ::= <expression> > <expression> { expression.val = Relational(expression1.val,expression2.val,'>') }
<expression> ::= INT { INT.val=int(20); expression.val = INT.val  }
<expression> ::= ID { ID.val='FECHA'; expression.val = ID.val  }
<type> ::= TIMESTAMP { type.val=['TIMESTAMP'] }
<columns> ::= <columns> ',' <column> { columns.val = columns.val.append(column.val) }
<column> ::= ID <type> <opt1> { ID.val='CLAVE'; column.val = ColumnId(ID.val, type.val, opt1.val) }
<opt1> ::= <checks> { opt1.val = checks.val }
<checks> ::= CONSTRAINT ID CHECK '(' <expression> ')' (<default>|<null>|<primarys>|<reference>|<uniques>) { ID.val='F_CALVE'; checks.val={'constraintcheck':[ID.val,expression.val]} + option.val }
<default> ::= DEFAULT <expression>  { default.val={'default':expression.val} }
<expression> ::= INT { INT.val=int(0); expression.val = INT.val  }
<expression> ::= <expression> > <expression> { expression.val = Relational(expression1.val,expression2.val,'>') }
<expression> ::= INT { INT.val=int(10); expression.val = INT.val  }
<expression> ::= ID { ID.val='CLAVE'; expression.val = ID.val  }
<type> ::= INTEGER { type.val=['INTEGER'] }
<columns> ::= <columns> ',' <column> { columns.val = columns.val.append(column.val) }
<column> ::= ID <type> <opt1> { ID.val='GRUPO'; column.val = ColumnId(ID.val, type.val, opt1.val) }
<opt1> ::= <uniques> { opt1.val = uniques.val }
<uniques> ::= CONSTRAINT ID UNIQUE { ID.val='F_GRUPO'; uniques.val={'constraintunique':ID.val} }
<type> ::= CHAR { type.val=['CHAR'] }
<columns> ::= <column> { columns.val = [column.val] }
<column> ::= ID <type> { ID.val='ID'; column.val = ColumnId(ID.val, type.val, None) }
<type> ::= INTEGER { type.val=['INTEGER'] }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <ddl> ';' { sentence.val = ddl.val }
<ddl> ::= <create> { ddl.val = create.val }
<create> ::= <createTable> { create.val = createTable.val }
<createTable> ::=  CREATE TABLE ID '(' <columns> ')' { ID.val='USUARIOS'; createTable.val = CreateTable(ID.val,columns.val,None); }
<columns> ::= <columns> ',' <column> { columns.val = columns.val.append(column.val) }
<column> ::= CONSTRAINT ID CHECK '(' <expression> ')' { ID.val='F_EDAD'; column.val = ColumnConstraint(ID.val,expression.val) }
<expression> ::= <expression> > <expression> { expression.val = Relational(expression1.val,expression2.val,'>') }
<expression> ::= INT { INT.val=int(18); expression.val = INT.val  }
<expression> ::= ID { ID.val='EDAD'; expression.val = ID.val  }
<columns> ::= <columns> ',' <column> { columns.val = columns.val.append(column.val) }
<column> ::= ID <type> { ID.val='EDAD'; column.val = ColumnId(ID.val, type.val, None) }
<type> ::= INTEGER { type.val=['INTEGER'] }
<columns> ::= <columns> ',' <column> { columns.val = columns.val.append(column.val) }
<column> ::= ID <type> <opt1> { ID.val='CLAVE'; column.val = ColumnId(ID.val, type.val, opt1.val) }
<opt1> ::= <uniques> { opt1.val = uniques.val }
<uniques> ::= UNIQUE (<default>|<null>|<primarys>|<reference>|<checks>) { uniques.val={'unique':True} + option.val }
<null> ::= NOT NULL (<default>|<primarys>|<reference>|<uniques>|<checks>) { null.val={'null':False} + option.val }
<default> ::= DEFAULT <expression>  { default.val={'default':expression.val} }
<expression> ::= INT { INT.val=int(4); expression.val = INT.val  }
<type> ::= VARCHAR '(' 10 ')' { type.val=['VARCHAR',10] }
<columns> ::= <columns> ',' <column> { columns.val = columns.val.append(column.val) }
<column> ::= ID <type> <opt1> { ID.val='NOMBRE'; column.val = ColumnId(ID.val, type.val, opt1.val) }
<opt1> ::= <default> { opt1.val = default.val }
<default> ::= DEFAULT <expression> (<null>|<primarys>|<reference>|<uniques>|<checks>) { default.val={'default':expression.val} + option.val }        
<uniques> ::= UNIQUE { uniques.val={'unique':True} }
<expression> ::= INT { INT.val=int(1234); expression.val = INT.val  }
<type> ::= VARCHAR '(' 8 ')' { type.val=['VARCHAR',8] }
<columns> ::= <column> { columns.val = [column.val] }
<column> ::= ID <type> <opt1> { ID.val='ID'; column.val = ColumnId(ID.val, type.val, opt1.val) }
<opt1> ::= <primarys> { opt1.val = primarys.val }
<primarys> ::= PRIMARY KEY { primarys.val={'primary':True} }
<type> ::= INTEGER { type.val=['INTEGER'] }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<dml> ::= <select> { dml.val = select.val }
<select> ::= <selectInstruction> { select.val=selectInstruction }
<selectInstruction> ::= SELECT DISTINCT <expressionList> FROM <expressionList> <selectOptions> { selectInstruction.val=Select(expressionList.val,True,expressionList.val,selectOptions.val) }
<selectOptions> ::= <selectOptions> <selectOption> { selectOptions.val=selectOptions1.val+selectOption.val }
<selectOption> ::= HAVING <expression> { selectOption.val={'having':expression.val} }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<selectOptions> ::= <selectOptions> <selectOption> { selectOptions.val=selectOptions1.val+selectOption.val }
<selectOption> ::= GROUP BY <expressionlist> { selectOption.val={'groupby':expressionlist.val} }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<selectOptions> ::= <selectOption> { selectOptions.val=selectOption.val }
<selectOption> ::= WHERE <expression> { selectOption.val={'where':expression.val} }
<expression> ::= <expression> = <expression> { expression.val = Relational(expression1.val,expression2.val,'=') }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<dml> ::= <select> { dml.val = select.val }
<select> ::= <selectInstruction> { select.val=selectInstruction }
<selectInstruction> ::= SELECT DISTINCT <expressionList> FROM <expressionList> <selectOptions> { selectInstruction.val=Select(expressionList.val,True,expressionList.val,selectOptions.val) }
<selectOptions> ::= <selectOptions> <selectOption> { selectOptions.val=selectOptions1.val+selectOption.val }
<selectOption> ::= HAVING <expression> { selectOption.val={'having':expression.val} }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<selectOptions> ::= <selectOptions> <selectOption> { selectOptions.val=selectOptions1.val+selectOption.val }
<selectOption> ::= GROUP BY <expressionlist> { selectOption.val={'groupby':expressionlist.val} }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<selectOptions> ::= <selectOption> { selectOptions.val=selectOption.val }
<selectOption> ::= WHERE <expression> { selectOption.val={'where':expression.val} }
<expression> ::= <expression> SIMILAR <expression> { expression.val = Range(expression1.val,expression2.val,'SIMILAR') }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<dml> ::= <select> { dml.val = select.val }
<select> ::= <selectInstruction> { select.val=selectInstruction }
<selectInstruction> ::= SELECT DISTINCT <expressionList> FROM <expressionList> <selectOptions> { selectInstruction.val=Select(expressionList.val,True,expressionList.val,selectOptions.val) }
<selectOptions> ::= <selectOptions> <selectOption> { selectOptions.val=selectOptions1.val+selectOption.val }
<selectOption> ::= HAVING <expression> { selectOption.val={'having':expression.val} }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<selectOptions> ::= <selectOptions> <selectOption> { selectOptions.val=selectOptions1.val+selectOption.val }
<selectOption> ::= GROUP BY <expressionlist> { selectOption.val={'groupby':expressionlist.val} }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<selectOptions> ::= <selectOption> { selectOptions.val=selectOption.val }
<selectOption> ::= WHERE <expression> { selectOption.val={'where':expression.val} }
<expression> ::= <expression> LIKE <expression> { expression.val = Range(expression1.val,expression2.val,'LIKE') }
<expression> ::= INT { INT.val=int(1); expression.val = INT.val  }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<dml> ::= <select> { dml.val = select.val }
<select> ::= <selectInstruction> { select.val=selectInstruction }
<selectInstruction> ::= SELECT DISTINCT <expressionList> FROM <expressionList> <selectOptions> { selectInstruction.val=Select(expressionList.val,True,expressionList.val,selectOptions.val) }
<selectOptions> ::= <selectOptions> <selectOption> { selectOptions.val=selectOptions1.val+selectOption.val }
<selectOption> ::= HAVING <expression> { selectOption.val={'having':expression.val} }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<selectOptions> ::= <selectOptions> <selectOption> { selectOptions.val=selectOptions1.val+selectOption.val }
<selectOption> ::= GROUP BY <expressionlist> { selectOption.val={'groupby':expressionlist.val} }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<selectOptions> ::= <selectOption> { selectOptions.val=selectOption.val }
<selectOption> ::= WHERE <expression> { selectOption.val={'where':expression.val} }
<expression> ::= <expression> != <expression> { expression.val = Relational(expression1.val,expression2.val,'!=') }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<dml> ::= <select> { dml.val = select.val }
<select> ::= <selectInstruction> { select.val=selectInstruction }
<selectInstruction> ::= SELECT DISTINCT <expressionList> FROM <expressionList> <selectOptions> { selectInstruction.val=Select(expressionList.val,True,expressionList.val,selectOptions.val) }
<selectOptions> ::= <selectOptions> <selectOption> { selectOptions.val=selectOptions1.val+selectOption.val }
<selectOption> ::= HAVING <expression> { selectOption.val={'having':expression.val} }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<selectOptions> ::= <selectOptions> <selectOption> { selectOptions.val=selectOptions1.val+selectOption.val }
<selectOption> ::= GROUP BY <expressionlist> { selectOption.val={'groupby':expressionlist.val} }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<selectOptions> ::= <selectOption> { selectOptions.val=selectOption.val }
<selectOption> ::= WHERE <expression> { selectOption.val={'where':expression.val} }
<expression> ::= <expression> <> <expression> { expression.val = Relational(expression1.val,expression2.val,'<>') }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<dml> ::= <select> { dml.val = select.val }
<select> ::= <select> EXCEPT <select> { select.val=SelectMultiple(select.val,'EXCEPT',select.val) }
<select> ::= <selectInstruction> { select.val=selectInstruction }
<selectInstruction> ::= SELECT DISTINCT <expressionList> FROM <expressionList> <selectOptions> { selectInstruction.val=Select(expressionList.val,True,expressionList.val,selectOptions.val) }
<selectOptions> ::= <selectOptions> <selectOption> { selectOptions.val=selectOptions1.val+selectOption.val }
<selectOption> ::= HAVING <expression> { selectOption.val={'having':expression.val} }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<selectOptions> ::= <selectOptions> <selectOption> { selectOptions.val=selectOptions1.val+selectOption.val }
<selectOption> ::= GROUP BY <expressionlist> { selectOption.val={'groupby':expressionlist.val} }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<selectOptions> ::= <selectOption> { selectOptions.val=selectOption.val }
<selectOption> ::= WHERE <expression> { selectOption.val={'where':expression.val} }
<expression> ::= <expression> = <expression> { expression.val = Relational(expression1.val,expression2.val,'=') }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<select> ::= <selectInstruction> { select.val=selectInstruction }
<selectInstruction> ::= SELECT <expressionList> FROM <expressionList> <selectOptions> { selectInstruction.val=Select(expressionList.val,False,expressionList.val,selectOptions.val) }
<selectOptions> ::= <selectOptions> <selectOption> { selectOptions.val=selectOptions1.val+selectOption.val }
<selectOption> ::= LIMIT <expression> { selectOption.val={'limit':expression.val} }
<expression> ::= <expression> + <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'+') }
<expression> ::= <expression> % <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'%') }
<expression> ::= INT { INT.val=int(2); expression.val = INT.val  }
<expression> ::= INT { INT.val=int(5); expression.val = INT.val  }
<expression> ::= <expression> + <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'+') }
<expression> ::= <expression> * <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'*') }
<expression> ::= INT { INT.val=int(3); expression.val = INT.val  }
<expression> ::= INT { INT.val=int(2); expression.val = INT.val  }
<expression> ::= INT { INT.val=int(1); expression.val = INT.val  }
<selectOptions> ::= <selectOptions> <selectOption> { selectOptions.val=selectOptions1.val+selectOption.val }
<selectOption> ::= ORDER BY <sortExpressionList> { selectOption.val={'orderby':sortExpressionList.val} }
<sortExpressionList> ::= <sortExpressionList> ',' <expression> { sortExpressionList.val = sortExpressionList1.val.append([expression.val,'ASC']) }   
<expression> ::= ID { ID.val='EMAIL'; expression.val = ID.val  }
<sortExpressionList> ::= <sortExpressionList> ',' <expression> ASC { sortExpressionList.val = sortExpressionList1.val.append([expression.val,'ASC']) 
}
<expression> ::= ID { ID.val='NAME'; expression.val = ID.val  }
<sortExpressionList> ::= <expression> DESC {  sortExpressionList.val = [[expression.val,'DESC']] }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<selectOptions> ::= <selectOption> { selectOptions.val=selectOption.val }
<selectOption> ::= WHERE <expression> { selectOption.val={'where':expression.val} }
<expression> ::= <expression> + <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'+') }
<expression> ::= INT { INT.val=int(1); expression.val = INT.val  }
<expression> ::= INT { INT.val=int(1); expression.val = INT.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='TABLE1'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<dml> ::= <select> { dml.val = select.val }
<select> ::= <select> EXCEPT <select> { select.val=SelectMultiple(select.val,'EXCEPT',select.val) }
<select> ::= <selectInstruction> { select.val=selectInstruction }
<selectInstruction> ::= SELECT DISTINCT <expressionList> FROM <expressionList> { selectInstruction.val=Select(expressionList.val,True,expressionList.val,None) }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<select> ::= <selectInstruction> { select.val=selectInstruction }
<selectInstruction> ::= SELECT <expressionList> FROM <expressionList> { selectInstruction.val=Select(expressionList.val,False,expressionList.val,None) }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='TABLE1'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<dml> ::= <select> { dml.val = select.val }
<select> ::= <select> EXCEPT <select> { select.val=SelectMultiple(select.val,'EXCEPT',select.val) }
<select> ::= <selectInstruction> { select.val=selectInstruction }
<selectInstruction> ::= SELECT DISTINCT <expressionList> FROM <expressionList> { selectInstruction.val=Select(expressionList.val,True,expressionList.val,None) }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<select> ::= <selectInstruction> { select.val=selectInstruction }
<selectInstruction> ::= SELECT <expressionList> FROM <expressionList> { selectInstruction.val=Select(expressionList.val,False,expressionList.val,None) }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='TABLE1'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<dml> ::= <select> { dml.val = select.val }
<select> ::= <select> INTERSECT <select> { select.val=SelectMultiple(select.val,'INTERSECT',select.val) }
<select> ::= <selectInstruction> { select.val=selectInstruction }
<selectInstruction> ::= SELECT DISTINCT <expressionList> FROM <expressionList> <selectOptions> { selectInstruction.val=Select(expressionList.val,True,expressionList.val,selectOptions.val) }
<selectOptions> ::= <selectOption> { selectOptions.val=selectOption.val }
<selectOption> ::= WHERE <expression> { selectOption.val={'where':expression.val} }
<expression> ::= <expression> = <expression> { expression.val = Relational(expression1.val,expression2.val,'=') }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<select> ::= <selectInstruction> { select.val=selectInstruction }
<selectInstruction> ::= SELECT <expressionList> FROM <expressionList> { selectInstruction.val=Select(expressionList.val,False,expressionList.val,None) }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='TABLE1'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='TABLE1'; expression.val = ID.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<dml> ::= <select> { dml.val = select.val }
<select> ::= <select> INTERSECT <select> { select.val=SelectMultiple(select.val,'INTERSECT',select.val) }
<select> ::= <selectInstruction> { select.val=selectInstruction }
<selectInstruction> ::= SELECT DISTINCT <expressionList> FROM <expressionList> { selectInstruction.val=Select(expressionList.val,True,expressionList.val,None) }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<select> ::= <selectInstruction> { select.val=selectInstruction }
<selectInstruction> ::= SELECT <expressionList> FROM <expressionList> { selectInstruction.val=Select(expressionList.val,False,expressionList.val,None) }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='TABLE1'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<dml> ::= <select> { dml.val = select.val }
<select> ::= <select> UNION <select> { select.val=SelectMultiple(select.val,'UNION',select.val) }
<select> ::= <selectInstruction> { select.val=selectInstruction }
<selectInstruction> ::= SELECT DISTINCT <expressionList> FROM <expressionList> { selectInstruction.val=Select(expressionList.val,True,expressionList.val,None) }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<select> ::= <selectInstruction> { select.val=selectInstruction }
<selectInstruction> ::= SELECT <expressionList> FROM <expressionList> { selectInstruction.val=Select(expressionList.val,False,expressionList.val,None) }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='TABLE1'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<dml> ::= <select> { dml.val = select.val }
<select> ::= <select> UNION <select> { select.val=SelectMultiple(select.val,'UNION',select.val) }
<select> ::= <selectInstruction> { select.val=selectInstruction }
<selectInstruction> ::= SELECT DISTINCT <expressionList> FROM <expressionList> { selectInstruction.val=Select(expressionList.val,True,expressionList.val,None) }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<select> ::= <selectInstruction> { select.val=selectInstruction }
<selectInstruction> ::= SELECT <expressionList> FROM <expressionList> { selectInstruction.val=Select(expressionList.val,False,expressionList.val,None) }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='TABLE1'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<dml> ::= <select> { dml.val = select.val }
<select> ::= <selectInstruction> { select.val=selectInstruction }
<selectInstruction> ::= SELECT DISTINCT <expressionList> FROM <expressionList> { selectInstruction.val=Select(expressionList.val,True,expressionList.val,None) }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= <expression> . <expression> { expression.val = NSeparator(expression1.val,expression2.val,'.') }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<expression> ::= ID { ID.val='T1'; expression.val = ID.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<dml> ::= <select> { dml.val = select.val }
<select> ::= <selectInstruction> { select.val=selectInstruction }
<selectInstruction> ::= SELECT <expressionList> FROM <expressionList> { selectInstruction.val=Select(expressionList.val,False,expressionList.val,None) }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='TABLE1'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='ID'; expression.val = ID.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <ddl> ';' { sentence.val = ddl.val }
<ddl> ::= <create> { ddl.val = create.val }
<create> ::= <createType> { create.val = createType.val }
<createType> ::= CREATE TYPE ID AS ENUM '(' <expressionList> ')' { ID.val='MOOD'; createType.val=CreateType(ID.val,expressionList.val) }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= <expression> - <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'-') }
<expression> ::= INT { INT.val=int(2); expression.val = INT.val  }
<expression> ::= <expression> * <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'*') }
<expression> ::= INT { INT.val=int(3); expression.val = INT.val  }
<expression> ::= <expression> / <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'/') }
<expression> ::= INT { INT.val=int(5); expression.val = INT.val  }
<expression> ::= INT { INT.val=int(4); expression.val = INT.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= + <expression> { expression.val = Unary(expression.val,'+') }
<expression> ::= INT { INT.val=int(1); expression.val = INT.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= - <expression> { expression.val = Unary(expression.val,'-') }
<expression> ::= INT { INT.val=int(2); expression.val = INT.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= <expression> + <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'+') }
<expression> ::= <expression> * <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'*') }
<expression> ::= INT { INT.val=int(3); expression.val = INT.val  }
<expression> ::= INT { INT.val=int(2); expression.val = INT.val  }
<expression> ::= INT { INT.val=int(1); expression.val = INT.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<dml> ::= <insert> { dml.val =insert.val }
<insert> ::= INSERT INTO ID '(' <idList> ')' VALUES '(' <expressionList> ')' { ID.val='TABLE1'; insert.val=Insert(ID.val,idList.val,expressionList.val) }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= <expression> - <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'-') }
<expression> ::= INT { INT.val=int(2); expression.val = INT.val  }
<expression> ::= <expression> * <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'*') }
<expression> ::= INT { INT.val=int(3); expression.val = INT.val  }
<expression> ::= <expression> / <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'/') }
<expression> ::= INT { INT.val=int(5); expression.val = INT.val  }
<expression> ::= INT { INT.val=int(4); expression.val = INT.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= + <expression> { expression.val = Unary(expression.val,'+') }
<expression> ::= INT { INT.val=int(1); expression.val = INT.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= - <expression> { expression.val = Unary(expression.val,'-') }
<expression> ::= INT { INT.val=int(2); expression.val = INT.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= <expression> + <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'+') }
<expression> ::= <expression> * <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'*') }
<expression> ::= INT { INT.val=int(3); expression.val = INT.val  }
<expression> ::= INT { INT.val=int(2); expression.val = INT.val  }
<expression> ::= INT { INT.val=int(1); expression.val = INT.val  }
<idList> ::= <idList> ',' ID { ID.val='RESTA'; idList.val = idList1.val.append(ID.val) }
<idList> ::= <idList> ',' ID { ID.val='SUMA'; idList.val = idList1.val.append(ID.val) }
<idList> ::= <idList> ',' ID { ID.val='NUMERO'; idList.val = idList1.val.append(ID.val) }
<idList> ::= ID { ID.val='ID'; idList.val = [ID.val] }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<dml> ::= <insert> { dml.val =insert.val }
<insert> ::= INSERT INTO ID VALUES '(' <expressionList> ')' { ID.val='TABLE1'; insert.val=InsertAll(ID.val,expressionList.val) }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= <expression> - <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'-') }
<expression> ::= INT { INT.val=int(2); expression.val = INT.val  }
<expression> ::= <expression> * <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'*') }
<expression> ::= INT { INT.val=int(3); expression.val = INT.val  }
<expression> ::= <expression> / <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'/') }
<expression> ::= INT { INT.val=int(5); expression.val = INT.val  }
<expression> ::= INT { INT.val=int(4); expression.val = INT.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= + <expression> { expression.val = Unary(expression.val,'+') }
<expression> ::= INT { INT.val=int(1); expression.val = INT.val  }
<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }
<expression> ::= - <expression> { expression.val = Unary(expression.val,'-') }
<expression> ::= INT { INT.val=int(2); expression.val = INT.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= <expression> + <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'+') }
<expression> ::= <expression> * <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'*') }
<expression> ::= INT { INT.val=int(3); expression.val = INT.val  }
<expression> ::= INT { INT.val=int(2); expression.val = INT.val  }
<expression> ::= INT { INT.val=int(1); expression.val = INT.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <ddl> ';' { sentence.val = ddl.val }
<ddl> ::= <create> { ddl.val = create.val }
<create> ::= <createDatabase> { create.val = createDatabase.val }
<createDatabase> ::= CREATE OR REPLACE DATABASE ID <ownerMode> { ID.val='BASE8'; createDatabase.val = CreateDatabase(ID.val,False,True,ownerMode.val); }
<ownerMode> ::=  <expression> {  }
<expression> ::= INT { INT.val=int(3); expression.val = INT.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <ddl> ';' { sentence.val = ddl.val }
<ddl> ::= <create> { ddl.val = create.val }
<create> ::= <createDatabase> { create.val = createDatabase.val }
<createDatabase> ::= CREATE DATABASE IF NOT EXISTS ID <ownerMode> { ID.val='BASE7'; createDatabase.val = CreateDatabase(ID.val,True,False,ownerMode.val); }
<ownerMode> ::=  <expression> {  }
<expression> ::= INT { INT.val=int(3); expression.val = INT.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <ddl> ';' { sentence.val = ddl.val }
<ddl> ::= <create> { ddl.val = create.val }
<create> ::= <createDatabase> { create.val = createDatabase.val }
<createDatabase> ::= CREATE DATABASE IF NOT EXISTS ID <ownerMode> { ID.val='BASE6'; createDatabase.val = CreateDatabase(ID.val,True,False,ownerMode.val); }
<ownerMode> ::= OWNER ID MODE <expression> { ID.val='US1'; ownerMode.val = [ID.val,expression.val]; }
<expression> ::= INT { INT.val=int(3); expression.val = INT.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <ddl> ';' { sentence.val = ddl.val }
<ddl> ::= <create> { ddl.val = create.val }
<create> ::= <createDatabase> { create.val = createDatabase.val }
<createDatabase> ::= CREATE DATABASE IF NOT EXISTS ID <ownerMode> { ID.val='BASE5'; createDatabase.val = CreateDatabase(ID.val,True,False,ownerMode.val); }
<ownerMode> ::= MODE <expression> { ownerMode.val = [None,expression.val] }
<expression> ::= INT { INT.val=int(3); expression.val = INT.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <ddl> ';' { sentence.val = ddl.val }
<ddl> ::= <create> { ddl.val = create.val }
<create> ::= <createDatabase> { create.val = createDatabase.val }
<createDatabase> ::= CREATE DATABASE IF NOT EXISTS ID { ID.val='BASE4'; createDatabase.val = CreateDatabase(ID.val,True,False,[None,None]); }        
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <ddl> ';' { sentence.val = ddl.val }
<ddl> ::= <create> { ddl.val = create.val }
<create> ::= <createDatabase> { create.val = createDatabase.val }
<createDatabase> ::= CREATE DATABASE ID <ownerMode> { ID.val=BASE3; createDatabase.val = CreateDatabase(ID.val,False,False,ownerMode.val); }
<ownerMode> ::= MODE EQUAL <expression> { ownerMode.val = [None,expression.val] }
<expression> ::= INT { INT.val=int(5); expression.val = INT.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <ddl> ';' { sentence.val = ddl.val }
<ddl> ::= <create> { ddl.val = create.val }
<create> ::= <createDatabase> { create.val = createDatabase.val }
<createDatabase> ::= CREATE DATABASE ID <ownerMode> { ID.val=BASE2; createDatabase.val = CreateDatabase(ID.val,False,False,ownerMode.val); }
<ownerMode> ::= MODE EQUAL <expression> { ownerMode.val = [None,expression.val] }
<expression> ::= INT { INT.val=int(1); expression.val = INT.val  }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <ddl> ';' { sentence.val = ddl.val }
<ddl> ::= <create> { ddl.val = create.val }
<create> ::= <createDatabase> { create.val = createDatabase.val }
<createDatabase> ::= CREATE DATABASE ID { ID.val='BASE1'; createDatabase.val = CreateDatabase(ID.val,False,False,[None,None]); }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<ddl> ::= <create> { ddl.val = create.val }
<alter> ::= <alterTable> { alter.val=alterTable.val }
<alterTable> ::=  ALTER TABLE ID DROP CONSTRAINT ID { ID1.val='TABLE1'; ID2.val='NEW_CONSTRAINT'; alterTable.val=AlterTableDropConstraint(ID1.val,ID2.val) }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<ddl> ::= <create> { ddl.val = create.val }
<alter> ::= <alterTable> { alter.val=alterTable.val }
<alterTable> ::= ALTER TABLE ID ALTER COLUMN ID SET NOT NULL { ID1.val='TABLE1'; ID2.val='TABLE1_ID'; alterTable.val=AlterTableAlterColumnSetNull(ID1.val,ID2.val,True) }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<ddl> ::= <create> { ddl.val = create.val }
<alter> ::= <alterTable> { alter.val=alterTable.val }
<alterDatabase> ::= ALTER TABLE ID ADD FOREIGN KEY '(' ID ')' REFERENCES ID '(' ID ')' { ID1.val='TABLE1'; ID2.val='TABLE1_ID'; ID3.val='TABLE1'; ID4.val='TABLE1_ID'; alterDatabase.val=AlterTableAddForeignKey(ID1.val,ID2.val,ID3.val,ID4.val) }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<ddl> ::= <create> { ddl.val = create.val }
<alter> ::= <alterTable> { alter.val=alterTable.val }
<alterDatabase> ::= ALTER TABLE ID ADD CONSTRAINT ID UNIQUE '(' ID ')' { ID1.val='TABLE1'; ID2.val='NEW_CONSTRAINT'; ID3.val='NEW_CONSTRAINT'; alterDatabase.val=AlterTableAddConstraintUnique(ID1.val,ID2.val,ID3.val) }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<ddl> ::= <create> { ddl.val = create.val }
<alter> ::= <alterTable> { alter.val=alterTable.val }
<alterDatabase> ::= ALTER TABLE ID DROP COLUMN ID { ID1.val='TABLE1'; ID2.val='TABLE1_ID'; alterDatabase.val=AlterTableDropColumn(ID1.val,ID2.val) } 
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <ddl> ';' { sentence.val = ddl.val }
<ddl> ::= <alter> { ddl.val = alter.val }
<alter> ::= <alterDatabase> { alter.val=alterDatabase.val }
<alterDatabase> ::= ALTER DATABASE ID OWNER TO ID { ID1.val='DB1'; ID2.val='DIEGO'; alterDatabase.val=AlterDatabaseOwner(ID1.val,ID2.val) }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <ddl> ';' { sentence.val = ddl.val }
<ddl> ::= <alter> { ddl.val = alter.val }
<alter> ::= <alterDatabase> { alter.val=alterDatabase.val }
<alterDatabase> ::= ALTER DATABASE ID RENAME TO ID { ID1.val='DB1'; ID2.val='DB3'; alterDatabase.val=AlterDatabaseRename(ID1.val,ID2.val) }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<dml> ::= <show> { dml.val = show.val }
<show> ::=  SHOW DATABASES { show.val=ShowDatabases() }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <ddl> ';' { sentence.val = ddl.val }
<ddl> ::= <use> { ddl.val = use.val }
<use> ::= USE ID { ID.val='DB1'; use.val=Use(ID.val) }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<ddl> ::= <create> { ddl.val = create.val }
<drop> ::= <dropTable> { drop.val=dropTable.val }
<dropTable> ::= DROP TABLE ID { ID.val='TABLE1'; dropTable.val=DropTable(ID.val) }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <ddl> ';' { sentence.val = ddl.val }
<ddl> ::= <drop> { ddl.val = drop.val }
<drop> ::= <dropDatabase> { drop.val=dropDatabase.val }
<dropDatabase> ::= DROP DATABASE IF EXISTS ID { ID.val='DB2'; dropDatabase.val=DropDatabase(ID.val,True) }
<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }
<sentence> ::= <ddl> ';' { sentence.val = ddl.val }
<ddl> ::= <drop> { ddl.val = drop.val }
<drop> ::= <dropDatabase> { drop.val=dropDatabase.val }
<dropDatabase> ::= DROP DATABASE ID { ID.val='DB1'; dropDatabase.val=DropDatabase(ID.val,False) }
<sentences> ::= <sentence> { setences.val = [sentence.val] }
<sentence> ::= <dml> ';' { sentence.val = dml.val }
<dml> ::= <select> { dml.val = select.val }
<select> ::= <selectInstruction> { select.val=selectInstruction }
<selectInstruction> ::= SELECT <expressionList> FROM <expressionList> { selectInstruction.val=Select(expressionList.val,False,expressionList.val,None) }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= ID { ID.val='DB2'; expression.val = ID.val  }
<expressionList> ::= <expression> { expressionList.val = [expression.val] }
<expression> ::= <expression> + <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'+') }
<expression> ::= INT { INT.val=int(1); expression.val = INT.val  }
<expression> ::= INT { INT.val=int(1); expression.val = INT.val  }
```
