CREATE OR REPLACE FUNCTION notify_asd()
  RETURNS trigger AS $$
DECLARE
BEGIN
  PERFORM pg_notify(
    CAST('notify_asd' AS text),
    row_to_json(NEW)::text);
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER notify_asd
  AFTER INSERT ON TABLE_NAME
  FOR EACH ROW
  EXECUTE PROCEDURE notify_asd();
