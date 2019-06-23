-- Pull the information from the environment variables
\set username `echo $USER_NAME`
\set db `echo $USER_DB`

\c :db :username

BEGIN;
CREATE TABLE "rating" (
    "id" serial NOT NULL PRIMARY KEY,
    "created_at" timestamp with time zone NOT NULL,
    "name" varchar(64) NOT NULL,
    "score" integer not null,
    "division" varchar(128)
);
COMMIT;

