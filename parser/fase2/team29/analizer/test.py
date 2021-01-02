import grammar2



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
    
    LOOP
       
        UPDATE db SET b = data WHERE a = key_;
        IF found2>5 THEN
            RETURN;
        END IF;        
            INSERT INTO db(a,b) VALUES (key_, data);
            RETURN;
    END LOOP;
    
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
    
    FOR r IN
        SELECT * FROM foo WHERE fooid > 0
    LOOP
        
        RETURN NEXT r; 
    END LOOP;
    
    RETURN QUERY SELECT flightid
                   FROM flight
                  WHERE flightdate >= $1
                    AND flightdate < ($1 + 1);
    
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

    LOOP
    IF count_ > 0 THEN
        EXIT; 
    END IF;

    END LOOP;

    LOOP
    
    EXIT WHEN count_ > 100;
    CONTINUE WHEN count_ < 50;
    
    END LOOP;

    LOOP
        
        EXIT WHEN count_ > 0;  
    END LOOP;

    WHILE amount_owed > 0 AND gift_certificate_balance > 0 LOOP
    
    END LOOP;

    WHILE 5 > 3 LOOP
        
    END LOOP;

    FOR i IN 1..10 LOOP
    
    END LOOP;

    FOR i IN REVERSE 10..1 LOOP
    END LOOP;

    FOR i IN REVERSE 10..1 BY 2 LOOP
    
    END LOOP;

    FOR mviews IN
       SELECT n.nspname AS mv_schema,
              c.relname AS mv_name,
              pg_catalog.pg_get_userbyid AS owner_
         FROM pg_class c
    LEFT JOIN pg_namespace n ON (n.oid = c.relnamespace)
        WHERE c.relkind = 'm'
     ORDER BY 1
    LOOP

    END LOOP;



    EXCEPTION WHEN unique_violation THEN
           NULL;
        
END;
"""
result = grammar2.parse(s)
print(result)