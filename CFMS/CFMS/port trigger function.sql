CREATE OR REPLACE FUNCTION port_audit_function()
RETURNS TRIGGER AS $$
BEGIN
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO port_portfolio (action, port_id, timestamp)
        VALUES ('INSERT', NEW.id, current_timestamp);
    ELSIF (TG_OP = 'UPDATE') THEN
        INSERT INTO port_portfolio (action, port_id, timestamp)
        VALUES ('UPDATE', NEW.id, current_timestamp);
    ELSIF (TG_OP = 'DELETE') THEN
        INSERT INTO port_portfolio (action, port_id, timestamp)
        VALUES ('DELETE', OLD.id, current_timestamp);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER port_audit_trigger
AFTER INSERT OR UPDATE OR DELETE ON project_app_port
FOR EACH ROW
EXECUTE FUNCTION port_audit_function();
