-- this sql script the full description
SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_schema = table_name = 'first_table';
SELECT column_name
FROM information_schema.key_column_usage
WHERE table_schema = table_name = 'first_table' AND constraint_name = 'PRIMARY';
SELECT index_name, column_name
FROM information_schema.statistics
WHERE table_schema =table_name = 'first_table';
