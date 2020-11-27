# SQL SYNTAX
Portion of PostgreSQL 13.1 Documentation [see LICENSE](LICENSE.md)

## Queries

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
... FROM table_reference [AS] alias
```

```sql
... FROM (SELECT * FROM table1) AS alias_name
```

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
 
 
## Doubts or ambiguities?
Any doubt or ambiguity consult the most recent [PostgreSQL documentation](https://www.postgresql.org/docs/current/sql.html). 


