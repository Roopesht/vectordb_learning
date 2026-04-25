create table docs (doctext varchar(255));

insert into docs (doctext) values ('🔍 What is a Vector Database?');
insert into docs (doctext) values ('Use Cases: Search, RAG, Recommendations');


select * from docs where doctext like '%Look%';

ID: 23948
Doc: What is a Vector Database?
Embeddings: [-3049, 2039.34, ]
metadata: [keyword: 'Vector Db']
