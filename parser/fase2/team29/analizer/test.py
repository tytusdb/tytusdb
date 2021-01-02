import grammarFP as grammar2



s = """ 
DECLARE
user_id integer;
quantity numeric(5);
url varchar;
myrow tablename%ROWTYPE;
myfield tablename.columnname%TYPE;
arow RECORD;
 v_string ALIAS FOR $1;
    index ALIAS FOR $2;
BEGIN
    sum_ := x + y;
    prod := x * y;
    
    
    RETURN QUERY SELECT s.quantity, s.quantity * s.price FROM sales AS s
                 WHERE s.itemno = p_itemno;
    
    result := v1 + v2 + v3;
    RETURN result;
    
    SELECT * INTO myrec FROM emp WHERE empname = myname;
    
    EXECUTE 'UPDATE tbl SET '
        || quote_ident(colname)
        || ' = '
        || quote_nullable(newvalue)
        || ' WHERE key = '
        || quote_nullable(keyvalue);
    GET DIAGNOSTICS integer_var = ROW_COUNT;
    
    
    RETURN QUERY SELECT flightid
                   FROM flight
                  WHERE flightdate >= var
                    AND flightdate < (alv + 1);
    
    IF v_count > 0 THEN
    INSERT INTO users_count (count_) VALUES (v_count);
    RETURN 't';
    ELSE
        RETURN 'f';
    END IF;

    IF number = 0 THEN
        result := 'zero';
    ELSIF number > 0 THEN
        result := 'positive';
    ELSIF number < 0 THEN
        result := 'negative';
    ELSE

        result := 'NULL';
    END IF;

    CASE x
    WHEN 1, 2 THEN
        msg := 'one or two';
    ELSE
        msg := 'other value than one or two';
    END CASE;

    CASE
    WHEN x BETWEEN 0 AND 10 THEN
        msg := 'value is between zero and ten';
    WHEN x BETWEEN 11 AND 20 THEN
        msg := 'value is between eleven and twenty';
    END CASE;



    EXCEPTION WHEN unique_violation THEN
           NULL;
        
END;
"""
result = grammar2.parse(s)
print(result)