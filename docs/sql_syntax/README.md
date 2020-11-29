# SQL SYNTAX
Portion of PostgreSQL 13.1 Documentation [see LICENSE](LICENSE.md)

## 1. General Information


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

### Subqueries

```sql
FROM table_reference [AS] alias
```

```sql
FROM (SELECT * FROM table1) AS alias_name
```

A scalar subquery is an ordinary SELECT query in parentheses that returns exactly one row with one column.

A subquery can also be a VALUES list.

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


