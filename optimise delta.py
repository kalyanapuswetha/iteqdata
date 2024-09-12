# Databricks notebook source
# MAGIC %sql
# MAGIC create table emp_2(id int,name string)

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into emp_2 values(101,'swetha')

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into emp_2 values(2,'aaaa'),(3,'bbb'),(4,'ccc');

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from emp_2
