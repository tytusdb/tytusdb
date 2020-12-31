 -- -----  Ejemplo de un If ---------
   

do $$
declare
  tax integer := 10;

begin  
  
  if tax > 5 then
     raise notice 'es mayor a %', tax;

     select * from table1;

     select()

  else 
     raise notice 'no es mayor  a %',tax;

  end if;
  
end $$
   
   
