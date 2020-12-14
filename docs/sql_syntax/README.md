# SQL SYNTAX
Portion of PostgreSQL 13.1 Documentation [see LICENSE](LICENSE.md)

This is a summary of the most important parts of the language, and which will be implemented.

## 1. General Information

### Numeric Types

Name | Storage Size | Description | Range
-----|--------------|-------------|------
smallint | 2 bytes | small-range integer | -32768 to +32767
integer|4 bytes|typical choice for integer|-2147483648 to +2147483647
bigint|8 bytes|large-range integer|-9223372036854775808 to +9223372036854775807
decimal|variable|user-specified precision, exact|up to 131072 digits before the decimal point; up to 16383 digits after the decimal point
numeric|variable|user-specified precision, exact|up to 131072 digits before the decimal point; up to 16383 digits after the decimal point
real|4 bytes|variable-precision, inexact|6 decimal digits precision
double precision|8 bytes|variable-precision, inexact|15 decimal digits precision
money|8 bytes|currency amount|-92233720368547758.08 to +92233720368547758.07

### Character types

Name|Description
----|-----------
character varying(n), varchar(n)|variable-length with limit
character(n), char(n)|fixed-length, blank padded
text|variable unlimited length

### Date/Time Types

Name|Storage Size|Description|Low Value|High Value	Resolution
----|------------|-----------|---------|----------------------
timestamp [ (p) ] [ without time zone ]|8 bytes|both date and time (no time zone)|4713 BC|294276 AD|1 microsecond
timestamp [ (p) ] with time zone|8 bytes|both date and time, with time zone|4713 BC|294276 AD|1 microsecond
date|4 bytes|date (no time of day)|4713 BC|5874897 AD|1 day
time [ (p) ] [ without time zone ]|8 bytes|time of day (no date)|00:00:00|24:00:00|1 microsecond
time [ (p) ] with time zone|12 bytes|time of day (no date), with time zone|00:00:00+1559|24:00:00-1559|1 microsecond
interval [ fields ] [ (p) ]|16 bytes|time interval|-178000000 years|178000000 years|1 microsecond

The interval type has an additional option, which is to restrict the set of stored fields by writing one of these phrases:

```
YEAR
MONTH
DAY
HOUR
MINUTE
SECOND
YEAR TO MONTH
DAY TO HOUR
DAY TO MINUTE
DAY TO SECOND
HOUR TO MINUTE
HOUR TO SECOND
MINUTE TO SECOND
```

### Boolean Type

Name|Storage Size|Description
----|------------|-----------
boolean|1 byte|state of true or false

The datatype input function for type boolean accepts these string representations for the “true” state:

true
yes
on
1

and these representations for the “false” state:

false
no
off
0

### Enumerated Type

```sql
CREATE TYPE mood AS ENUM ('sad', 'ok', 'happy');
```

### Comments
```
-- This is a standard SQL comment
```

```
/* multiline comment
 * with nesting: /* nested block comment */
 */
```

### Operator Precedence

Operator/Element | Associativity | Description
-----------------|---------------|------------
. | left | table/column name separator
:: | left | PostgreSQL-style typecast
[ ] | left | array element selection
\+ \- | right | unary plus, unary minus
^ | left | exponentiation
\* / % | left | multiplication, division, modulo
\+ \- | left | addition, subtraction
(any other operator) | left | all other native and user-defined operators
BETWEEN IN LIKE ILIKE SIMILAR | | range containment, set membership, string matching
< > = <= >= <> | | comparison operators
IS ISNULL NOTNULL | | IS TRUE, IS FALSE, IS NULL, IS DISTINCT FROM, etc
NOT | right | logical negation
AND | left | logical conjunction
OR | left | logical disjunction


### Escape Sequence
Backslash Escape Sequence | Interpretation
--------------------------|---------------
\b | backspace
\f | form feed
\n | newline
\r | carriage return
\t | tab
\o, \oo, \ooo (o = 0–7) | octal byte value
\xh, \xhh (h = 0–9, A–F) | hexadecimal byte value
\uxxxx, \Uxxxxxxxx (x = 0–9, A–F) | 16 or 32-bit hexadecimal Unicode character value

### Numeric constant

```
digits
digits.[digits][e[+-]digits]
[digits].digits[e[+-]digits]
digitse[+-]digits
```

## 2. Definition

```sql
CREATE [OR REPLACE] DATABASE [IF NOT EXISTS] name
    [ OWNER [=] user_name ]
    [ MODE [=] mode_number ]
```
Mode default = 1

```sql
SHOW DATABASES [LIKE regex]
```

```sql
ALTER DATABASE name RENAME TO new_name

ALTER DATABASE name OWNER TO { new_owner | CURRENT_USER | SESSION_USER }
```

```sql
DROP DATABASE [ IF EXISTS ] name
```

```sql
USE databasename
```
In theory, PostgreSQL cannot switch between databases, it must be disconnected and connected from the client. But for this phase the DBMS client is not yet available, so the use of the USE statement will be accepted.  

```sql
CREATE TABLE my_first_table (
    column1 type [DEFAULT value] [[NOT] NULL] [[CONSTRAINT name] UNIQUE] [[CONSTRAINT name] CHECK (condition_column1)]
    [, column2...]
    [, [CONSTRAINT name] CHECK (condition_many_columns)...]
    [, UNIQUE (column1 [, column2]...)]
);
```
A primary key constraint indicates that a column, or group of columns, can be used as a unique identifier for rows in the table. This requires that the values be both unique and not null.

```sql
CREATE TABLE my_first_table (
    column1 type [PRIMARY KEY]
    [, column2 type [REFERENCES table]]
    [, column3...]
);
```

```sql
CREATE TABLE my_first_table (
    column1 type
    [, column2...]
    [, [PRIMARY KEY (column1,..., column_n)]
    [, [FOREIGN KEY (column1,..., column_n) REFERENCES table (column1_other,..., column_n_other)]
);
```

```sql
DROP TABLE my_first_table;
```

```sql
ALTER TABLE table ADD COLUMN column type;
```

```sql
ALTER TABLE products DROP COLUMN description;
```

```sql
ALTER TABLE table ADD CHECK (name <> '');
ALTER TABLE table ADD CONSTRAINT some_name UNIQUE (column);
ALTER TABLE table ADD FOREIGN KEY (column_group_id) REFERENCES column_groups;
ALTER TABLE table ALTER COLUMN column SET NOT NULL;
ALTER TABLE table DROP CONSTRAINT some_name;
ALTER TABLE table RENAME COLUMN column1 TO column1_1;
[... ;]
```

```sql
DELETE FROM [ ONLY ] table_name [ * ] [ [ AS ] alias ]
    [ USING from_item [, ...] ]
    [ WHERE condition | WHERE CURRENT OF cursor_name ]
    [ RETURNING * | output_expression [ [ AS ] output_name ] [, ...] ]
```

### Inheritance

```sql
CREATE TABLE cities (
    name            text,
    population      float,
    elevation       int     -- in feet
);

CREATE TABLE capitals (
    state           char(2)
) INHERITS (cities);
```

### Data Manipulation

```sql
INSERT INTO products VALUES (1, 'Cheese', 9.99);
```

```sql
UPDATE products SET price = 10 WHERE price = 5;
```

```sql
DELETE FROM products WHERE price = 10;
```

More examples in [dml documentation](https://www.postgresql.org/docs/current/dml.html)

## 3. Queries

### Query structure

```sql
SELECT [DISTINCT] select_list FROM table_expression 
[WHERE search_condition] 
[GROUP BY grouping_column_reference [, grouping_column_reference]...]
```

The select list specification * means all columns that the table expression happens to provide. A select list can also select a subset of the available columns or make calculations using the columns.

In general, table expressions can be complex constructs of base tables, joins, and subqueries. But you can also omit the table expression entirely and use the SELECT command as a calculator.

If more than one table has a column of the same name, the table name must also be given. (.)

Column lables: if no output column name is specified using AS. The AS keyword is optional, but only if the new column name does not match any SQL keyword.

Where search_condition is any value expression that returns a value of type boolean.

After passing the WHERE filter, the derived input table might be subject to grouping, using the GROUP BY clause, and elimination of group rows using the HAVING clause.

```sql
SELECT select_list FROM ... [WHERE ...] GROUP BY ... HAVING boolean_expression
```

### Logical Operators

The usual logical operators are available:

```
boolean AND boolean → boolean
boolean OR boolean → boolean
NOT boolean → boolean
```

SQL uses a three-valued logic system with true, false, and null, which represents “unknown”.

### Comparison Operators

Operator|Description
--------|-----------
datatype < datatype → boolean|Less than
datatype > datatype → boolean|Greater than
datatype <= datatype → boolean|Less than or equal to
datatype >= datatype → boolean|Greater than or equal to
datatype = datatype → boolean|Equal
datatype <> datatype → boolean|Not equal
datatype != datatype → boolean|Not equal

### Comparison Predicates

Predicate
Description
Example(s)

datatype BETWEEN datatype AND datatype → boolean
Between (inclusive of the range endpoints).
2 BETWEEN 1 AND 3 → t
2 BETWEEN 3 AND 1 → f

datatype NOT BETWEEN datatype AND datatype → boolean
Not between (the negation of BETWEEN).
2 NOT BETWEEN 1 AND 3 → f

datatype BETWEEN SYMMETRIC datatype AND datatype → boolean
Between, after sorting the two endpoint values.
2 BETWEEN SYMMETRIC 3 AND 1 → t

datatype NOT BETWEEN SYMMETRIC datatype AND datatype → boolean
Not between, after sorting the two endpoint values.
2 NOT BETWEEN SYMMETRIC 3 AND 1 → f

datatype IS DISTINCT FROM datatype → boolean
Not equal, treating null as a comparable value.
1 IS DISTINCT FROM NULL → t (rather than NULL)
NULL IS DISTINCT FROM NULL → f (rather than NULL)

datatype IS NOT DISTINCT FROM datatype → boolean
Equal, treating null as a comparable value.
1 IS NOT DISTINCT FROM NULL → f (rather than NULL)
NULL IS NOT DISTINCT FROM NULL → t (rather than NULL)

datatype IS NULL → boolean
Test whether value is null.
1.5 IS NULL → f

datatype IS NOT NULL → boolean
Test whether value is not null.
'null' IS NOT NULL → t

datatype ISNULL → boolean
Test whether value is null (nonstandard syntax).

datatype NOTNULL → boolean
Test whether value is not null (nonstandard syntax).

boolean IS TRUE → boolean
Test whether boolean expression yields true.
true IS TRUE → t
NULL::boolean IS TRUE → f (rather than NULL)

boolean IS NOT TRUE → boolean
Test whether boolean expression yields false or unknown.
true IS NOT TRUE → f
NULL::boolean IS NOT TRUE → t (rather than NULL)

boolean IS FALSE → boolean
Test whether boolean expression yields false.
true IS FALSE → f
NULL::boolean IS FALSE → f (rather than NULL)

boolean IS NOT FALSE → boolean
Test whether boolean expression yields true or unknown.
true IS NOT FALSE → t
NULL::boolean IS NOT FALSE → t (rather than NULL)

boolean IS UNKNOWN → boolean
Test whether boolean expression yields unknown.
true IS UNKNOWN → f
NULL::boolean IS UNKNOWN → t (rather than NULL)

boolean IS NOT UNKNOWN → boolean
Test whether boolean expression yields true or false.
true IS NOT UNKNOWN → t
NULL::boolean IS NOT UNKNOWN → f (rather than NULL)

### Aggregate Functions

Like most other relational database products, PostgreSQL supports aggregate functions. An aggregate function computes a single result from multiple input rows. For example, there are aggregates to compute the count, sum, avg (average), max (maximum) and min (minimum) over a set of rows.

It is important to understand the interaction between aggregates and SQL's WHERE and HAVING clauses. The fundamental difference between WHERE and HAVING is this: WHERE selects input rows before groups and aggregates are computed (thus, it controls which rows go into the aggregate computation), whereas HAVING selects group rows after groups and aggregates are computed. Thus, the WHERE clause must not contain aggregate functions; it makes no sense to try to use an aggregate to determine which rows will be inputs to the aggregates. On the other hand, the HAVING clause always contains aggregate functions. (Strictly speaking, you are allowed to write a HAVING clause that doesn't use aggregates, but it's seldom useful. The same condition could be used more efficiently at the WHERE stage.)

### Mathematical Functions

abs, cbrt, ceil, ceiling, degrees, div, exp, factorial, floor, gcd, lcm, ln, log, log10, min_scale, mod, pi, power, radians, round, scale, sign, sqrt, trim_scale, truc, width_bucket, random, setseed

### Trigonometric Functions

acos, acosd, asin, asind, atan, atand, atan2, atan2d, cos, cosd, cot, cotd, sin, sind, tan, tand, sinh, cosh, tanh, asinh, acosh, atanh

### Binary String Functions

||, length, substring, trim, get_byte, md5, set_byte, sha256, substr, convert, encode, decode

Operators:

||, &,  |, #, ~, >>, <<

### Pattern Matching

LIKE, NOT LIKE, include regular expressions.

```sql
string LIKE pattern [ESCAPE escape-character]

string NOT LIKE pattern [ESCAPE escape-character]

substring(string, pattern, escape-character)
```

See Table 9.17. Regular Expression Atoms, Table 9.18. Regular Expression Quantifiers and Table 9.19. Regular Expression Constraints.

### Date/Time Functions

See [Date/Time Functions](https://www.postgresql.org/docs/current/functions-datetime.html)


### Subqueries

```sql
FROM table_reference [AS] alias
```

```sql
FROM (SELECT * FROM table1) AS alias_name
```

A scalar subquery is an ordinary SELECT query in parentheses that returns exactly one row with one column.

A subquery can also be a VALUES list.

```sql
EXISTS (subquery)

expression IN (subquery)

expression NOT IN (subquery)

row_constructor operator ANY (subquery)

expression operator ALL (subquery)

row_constructor operator SOME (subquery)
```

### Joins

```sql
T1 { [INNER] | { LEFT | RIGHT | FULL } [OUTER] } JOIN T2 ON boolean_expression
T1 { [INNER] | { LEFT | RIGHT | FULL } [OUTER] } JOIN T2 USING ( join column list )
T1 NATURAL { [INNER] | { LEFT | RIGHT | FULL } [OUTER] } JOIN T2
```

Joins of all types can be chained together, or nested: either or both T1 and T2 can be joined tables. Parentheses can be used around JOIN clauses to control the join order. In the absence of parentheses, JOIN clauses nest left-to-right.

### Sorting rows

```sql
SELECT select_list
    FROM table_expression
    ORDER BY sort_expression1 [ASC | DESC] [NULLS { FIRST | LAST }]
             [, sort_expression2 [ASC | DESC] [NULLS { FIRST | LAST }] ...]
```

### Expressions

```sql
CASE WHEN condition THEN result
     [WHEN ...]
     [ELSE result]
END
```

```sql
GREATEST(value [, ...])

LEAST(value [, ...])
```



### Limit and offset

```sql
SELECT select_list
    FROM table_expression
    [ ORDER BY ... ]
    [ LIMIT { number | ALL } ] [ OFFSET number ]
```

### Combining queries

```sql
query1 UNION [ALL] query2
query1 INTERSECT [ALL] query2
query1 EXCEPT [ALL] query2
```
 Set operations can also be nested and chained. ()
 
 
## 4. Doubts or ambiguities?
Any doubt or ambiguity consult the most recent [PostgreSQL documentation](https://www.postgresql.org/docs/current/sql.html). 


