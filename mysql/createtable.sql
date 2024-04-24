create table computing_list
(
   id         int unsigned not null auto_increment primary key,
   Type       text not null,
   User_name  text not null,
   Solver     text not null,
   Random     int not null,
   Amount     int unsigned null default 0,
   Case_name  varchar(50) null default 'Testcase',
   Time       datetime  not null
);
