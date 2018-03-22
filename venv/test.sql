CREATE OR REPLACE FUNCTION notify_pricesinserted()
  RETURNS trigger AS $$
DECLARE
BEGIN
  PERFORM pg_notify(
    CAST('pricesinserted' AS text),
    row_to_json(NEW)::text);
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER notify_pricesinserted
  AFTER INSERT ON COMPANY
  FOR EACH ROW
  EXECUTE PROCEDURE notify_pricesinserted();
