set serveroutput on

declare
v_empname employees.first_name%type:='Steve';
v_hiredate employees.hire_date%type:=sysdate;
v_empname employees.first_name%type:='';
v_empid number(5):=902;
v_empidnew number(5);

begin
select count(employee_id) into v_empidnew from employees where employee_id=v_empid;
if(v_empidnew=0) then
dbms_output.put_line('Employee does not exists');
else
update departments set MANAGER_ID=v_empid where department_name='IT';
end if;
end;

