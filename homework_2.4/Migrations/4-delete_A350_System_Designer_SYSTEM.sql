--ROLE SYSYTEM DESIGNER SYSTEM
--Delete the role A400M_System_Designer_SYSTEM
--Declaration of variables

DECLARE @CONTEXT_id_old INT
DECLARE @CONTEXT_id INT
DECLARE @FEATURE_id INT
DECLARE @FEATURE_FEATURE_GROUP_id INT
DECLARE @USER_id INT
---------------------------------------------------------------------------------
select @CONTEXT_id_old= CONTEXT_id FROM T_EDIP_CONTEXT WHERE ContextName='A400M_System_Designer_SYSTEM'

-- curser for have list of user which have this role
DECLARE list_user_System_Designer_SYSTEM CURSOR FOR 
	select CONTEXT__USER_USER_idr from dbo.T_LINK_CONTEXT__USER where CONTEXT__USER_CONTEXT_idr=@CONTEXT_id_old

-- 
IF EXISTS(SELECT * FROM T_EDIP_LINK_CONTEXT__FEATURE WHERE CONTEXT__FEATURE_CONTEXT_idr=@CONTEXT_id_old)
BEGIN
DELETE FROM T_EDIP_LINK_CONTEXT__FEATURE WHERE CONTEXT__FEATURE_CONTEXT_idr=@CONTEXT_id_old
END
IF EXISTS(SELECT * FROM T_EDIP_LINK_ATTRIBUTE__CONTEXT WHERE ATTRIBUTE__CONTEXT_CONTEXT_idr=@CONTEXT_id_old)
BEGIN
DELETE FROM T_EDIP_LINK_ATTRIBUTE__CONTEXT WHERE ATTRIBUTE__CONTEXT_CONTEXT_idr=@CONTEXT_id_old
END
IF EXISTS(SELECT * FROM T_LINK_CONTEXT__USER WHERE CONTEXT__USER_CONTEXT_idr=@CONTEXT_id_old)
BEGIN
DELETE FROM T_LINK_CONTEXT__USER WHERE CONTEXT__USER_CONTEXT_idr=@CONTEXT_id_old
END
IF EXISTS(SELECT * FROM T_EDIP_CONTEXT WHERE ContextName='A400M_System_Designer_SYSTEM')
BEGIN
DELETE FROM T_EDIP_CONTEXT WHERE ContextName='A400M_System_Designer_SYSTEM'
END
------------------------------------------------------------------------------------
--Give access rights assigned to the role A400M_System_Designer_SYSTEM to role A400M_Designer_SYSTEM
--Get the new role id
SELECT @CONTEXT_id=CONTEXT_id FROM T_EDIP_CONTEXT WHERE ContextName='A400M_Designer_SYSTEM' 
--Access for the feature Request Validation	(For BDDS)
SELECT @FEATURE_FEATURE_GROUP_id=FEATURE_GROUP_id FROM T_EDIP_FEATURE_GROUP WHERE FeatureGroupLabel='BDDS'
SELECT @FEATURE_id=FEATURE_id FROM T_EDIP_FEATURE WHERE FeatureLabel='Request Validation' AND FEATURE_FEATURE_GROUP_idr=@FEATURE_FEATURE_GROUP_id
IF(NOT EXISTS(SELECT * FROM T_EDIP_LINK_CONTEXT__FEATURE WHERE CONTEXT__FEATURE_CONTEXT_idr=@CONTEXT_id AND CONTEXT__FEATURE_FEATURE_idr=@FEATURE_id))
BEGIN
INSERT INTO T_EDIP_LINK_CONTEXT__FEATURE VALUES (@CONTEXT_id,@FEATURE_id,1)
END
ELSE
BEGIN
UPDATE T_EDIP_LINK_CONTEXT__FEATURE SET ContextFeatureAvailability=1
END
------------------------------------------------------------------------------------
--Access for the feature Request Validation	(For FDDS)
SELECT @FEATURE_FEATURE_GROUP_id=FEATURE_GROUP_id FROM T_EDIP_FEATURE_GROUP WHERE FeatureGroupLabel='FDDS'
SELECT @FEATURE_id=FEATURE_id FROM T_EDIP_FEATURE WHERE FeatureLabel='Request Validation' AND FEATURE_FEATURE_GROUP_idr=@FEATURE_FEATURE_GROUP_id
IF(NOT EXISTS(SELECT * FROM T_EDIP_LINK_CONTEXT__FEATURE WHERE CONTEXT__FEATURE_CONTEXT_idr=@CONTEXT_id AND CONTEXT__FEATURE_FEATURE_idr=@FEATURE_id))
BEGIN
INSERT INTO T_EDIP_LINK_CONTEXT__FEATURE VALUES (@CONTEXT_id,@FEATURE_id,1)
END
ELSE
BEGIN
UPDATE T_EDIP_LINK_CONTEXT__FEATURE SET ContextFeatureAvailability=1
END

------------------------------------------------------------------------------
--Users having the role “A400M_System_Designer_SYSTEM” should have the role “A400M_Designer_SYSTEM
-------------------------------------------------------------------------------
OPEN list_user_System_Designer_SYSTEM

FETCH list_user_System_Designer_SYSTEM INTO @USER_id

WHILE @@FETCH_STATUS = 0
BEGIN
	IF (NOT EXISTS(SELECT * FROM T_LINK_CONTEXT__USER WHERE CONTEXT__USER_CONTEXT_idr=@CONTEXT_id AND CONTEXT__USER_USER_idr=@USER_id))
	BEGIN
	INSERT INTO T_LINK_CONTEXT__USER (CONTEXT__USER_CONTEXT_idr,CONTEXT__USER_USER_idr) VALUES (@CONTEXT_id,@USER_id)
	END

	FETCH list_user_System_Designer_SYSTEM INTO @USER_id
END

CLOSE list_user_System_Designer_SYSTEM
DEALLOCATE list_user_System_Designer_SYSTEM