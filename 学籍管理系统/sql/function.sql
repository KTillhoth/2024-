USE SchoolManagement;
drop function if exists findmajor;
DELIMITER //
create function findmajor (id varchar(50))
returns varchar(50)
reads sql data
begin
	declare major_name varchar(50);
	select name from majors where major_id = id into major_name;  
    return major_name;
end//

DELIMITER ;
drop  function if exists finddepart;
DELIMITER //
create function finddepart ( id varchar(50))
returns varchar(50)
reads sql data
begin
	 declare depart_name varchar(50);
	select name from Departments where department_id = id into depart_name;  
    return depart_name;
end//

DELIMITER ;
drop trigger if exists major_num_u;
DELIMITER //
create trigger major_num_u after update on Students for each row
label:begin
	declare n_did,o_did varchar(50);
	if old.major_id=new.major_id then
		leave label;
	end if;
    select department_id from majors
	where major_id = old.major_id into o_did;
	select department_id from majors
	where major_id = new.major_id into n_did;
    Update Majors 
    set num = num-1
    where major_id = old.major_id;
    Update Majors 
    set num = num+1
    where major_id = new.major_id;
    if o_did=n_did then
		leave label;
	end if;
    Update  Departments 
    set num = num-1
    where department_id = o_did;
	Update  Departments 
    set num = num+1
    where department_id = n_did;
end//

DELIMITER ;
drop trigger if exists  major_num_i;
DELIMITER //
create trigger major_num_i after insert on Students for each row
begin
	  declare did varchar(50);
      Update Majors 
	  set num = num+1
	  where major_id = new.major_id;
      
	  select department_id from majors
      where major_id = new.major_id into did;
      Update  Departments 
	  set num = num+1
      where department_id = did;
end//

DELIMITER ;
drop procedure if exists updatemajor;
DELIMITER //
create procedure updatemajor (IN id varchar(50))
begin
	declare nem varchar(50);
    select new_major
    from students
	where student_id = id
    into nem;
	update Students 
    set major_id = nem,new_major=null
    where student_id = id;
end //

DELIMITER ;
drop procedure if exists deletecourse;
DELIMITER //
create procedure deletecourse (IN cid varchar(50))
begin
	declare num INT;
    start transaction;
    SELECT COUNT(*) 
	FROM grades
	WHERE course_id = cid AND grade IS NOT NULL
    into num;
    delete from grades
    where course_id = cid;
    delete from courses
	where course_id = cid;
    if num=0 then
		commit;
	else
		rollback;
    end if;
end //
DELIMITER ;

