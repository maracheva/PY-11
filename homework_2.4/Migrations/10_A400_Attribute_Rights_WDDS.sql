-- Role Data Admin – Attributes rights - WDDS

DECLARE @POR_ATTRIBUTE_id int
DECLARE @C_ATTRIBUTE_id int
DECLARE @CONTEXT_id INT

SELECT @CONTEXT_id = CONTEXT_id FROM T_EDIP_CONTEXT WHERE ContextName='A400M_Admin_data'
SELECT @POR_ATTRIBUTE_id = ATTRIBUTE_id FROM T_EDIP_ATTRIBUTE WHERE AttributeLabel = 'PDDS Origin' AND AttributeName = 'WDDSOriginPDDS'
SELECT @C_ATTRIBUTE_id = ATTRIBUTE_id FROM T_EDIP_ATTRIBUTE WHERE AttributeLabel = 'Is this a cancelled drawing ?' AND AttributeName = 'WDDSCancelled'



IF NOT EXISTS(SELECT * FROM T_EDIP_LINK_ATTRIBUTE__CONTEXT WHERE ATTRIBUTE__CONTEXT_ATTRIBUTE_idr=@POR_ATTRIBUTE_id AND ATTRIBUTE__CONTEXT_CONTEXT_idr=@CONTEXT_id)
BEGIN
INSERT INTO T_EDIP_LINK_ATTRIBUTE__CONTEXT 
(ATTRIBUTE__CONTEXT_ATTRIBUTE_idr, ATTRIBUTE__CONTEXT_CONTEXT_idr, AttributeContextReadMode, AttributeContextWriteMode) 
VALUES
(@POR_ATTRIBUTE_id, @CONTEXT_id, 1, 1)
END
ELSE
BEGIN
UPDATE T_EDIP_LINK_ATTRIBUTE__CONTEXT SET AttributeContextReadMode =1, AttributeContextWriteMode=1 WHERE
ATTRIBUTE__CONTEXT_ATTRIBUTE_idr=@POR_ATTRIBUTE_id AND ATTRIBUTE__CONTEXT_CONTEXT_idr=@CONTEXT_id
END




IF NOT EXISTS(SELECT * FROM T_EDIP_LINK_ATTRIBUTE__CONTEXT WHERE ATTRIBUTE__CONTEXT_ATTRIBUTE_idr=@C_ATTRIBUTE_id AND ATTRIBUTE__CONTEXT_CONTEXT_idr=@CONTEXT_id)
BEGIN
INSERT INTO T_EDIP_LINK_ATTRIBUTE__CONTEXT 
(ATTRIBUTE__CONTEXT_ATTRIBUTE_idr, ATTRIBUTE__CONTEXT_CONTEXT_idr, AttributeContextReadMode, AttributeContextWriteMode) 
VALUES
(@C_ATTRIBUTE_id, @CONTEXT_id, 1, 1)
END
ELSE
BEGIN
UPDATE T_EDIP_LINK_ATTRIBUTE__CONTEXT SET AttributeContextReadMode =1, AttributeContextWriteMode=1 WHERE
ATTRIBUTE__CONTEXT_ATTRIBUTE_idr=@C_ATTRIBUTE_id AND ATTRIBUTE__CONTEXT_CONTEXT_idr=@CONTEXT_id
END
