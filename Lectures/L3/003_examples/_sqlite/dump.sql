BEGIN TRANSACTION;
CREATE TABLE "users" (
           id INTEGER PRIMARY KEY,
           first_name VARCHAR(30) NOT NULL,
           last_name VARCHAR(30),
           birthday VARCHAR(30)
   );
INSERT INTO "users" VALUES(1,'Eugene','Hatsko','09-11-1992');
INSERT INTO "users" VALUES(2,'Dmitry','Ivanov','01-09-1993');
COMMIT;
