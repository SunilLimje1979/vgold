from django.db import models

# Create your models here.

class Countries(models.Model):
    id = models.AutoField(primary_key=True)
    sortname = models.CharField(max_length=3)
    name = models.CharField(max_length=150)
    phonecode = models.IntegerField()

    class Meta:
        
        db_table = 'countries'

class States(models.Model):
    id = models.AutoField(primary_key=True)
    sortname = models.CharField(max_length=3)
    name = models.CharField(max_length=150)
    phonecode = models.IntegerField()

    class Meta:
        
        db_table = 'states'
        
class Cities(models.Model):
    id = models.AutoField(primary_key=True)
    sortname = models.CharField(max_length=3)
    name = models.CharField(max_length=150)
    phonecode = models.IntegerField()

    class Meta:
        
        db_table = 'cities'



class tblUsers(models.Model):
    User_Id = models.AutoField(primary_key=True)
    
    UserFirstname = models.CharField(max_length=50, blank=True, null=True)
    UserMiddlename = models.CharField(max_length=50, blank=True, null=True)
    UserLastname = models.CharField(max_length=50, blank=True, null=True)
    UserCompnayName = models.CharField(max_length=100, blank=True, null=True)
    UserPannumber = models.CharField(max_length=10, blank=True, null=True)
    UserAadharNumber = models.CharField(max_length=16, blank=True, null=True)
    UserGSTNumber = models.CharField(max_length=30, blank=True, null=True)
    UserMobileNo = models.BigIntegerField(blank=True, null=True)
    UseralternateNo = models.BigIntegerField(blank=True, null=True)
    UserEmail = models.CharField(max_length=100, blank=True, null=True)
    UserDateofBirth = models.IntegerField(blank=True, null=True)
    UserAnniversaryDate = models.IntegerField(blank=True, null=True)
    UserQRCodeImage = models.CharField(max_length=100, blank=True, null=True)
    UserGender = models.IntegerField(blank=True, null=True,db_comment='1=>Male, 2=>Female')
    UserMarritalStatus = models.IntegerField(blank=True, null=True,db_comment='1=>Single, 2=>Married, 3=>Widow, 4=>Divorcy')
    
    UserRole = models.IntegerField(blank=True, null=True,db_comment='0=>Super Admin, 1=>Admin, 2=>Manager, 3=>Supervisor, 4=>Account, 5=> ChannelPartner, 6=> Member')
    UserChannelPartnerCode = models.CharField(max_length=10, blank=True, null=True)
    UserChannelPartnerOn = models.IntegerField(blank=True, null=True)
    UserPassword = models.CharField(max_length=20, blank=True, null=True)
    UserStatus = models.IntegerField(db_comment='1=>Active, 0=>Deactive,2=>Blocked ')
    UserAddress = models.CharField(max_length=200, blank=True, null=True)
    UserCityId = models.ForeignKey(Cities, on_delete=models.SET_NULL, null=True)
    UserStateId = models.ForeignKey(States, on_delete=models.SET_NULL, null=True)
    UserCountryId = models.ForeignKey(Countries, on_delete=models.SET_NULL, null=True)
    UserPincode = models.CharField(max_length=7, blank=True, null=True)
    
    UserReferanceCode = models.CharField(max_length=10, blank=True, null=True)
    UserParrentId = models.CharField(max_length=10, blank=True, null=True)
    # UserReferralId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True)
    UserAddedOn = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'tblUsers'


# Create your models here.
class tblSystemParameters(models.Model):
    SystemParameter_Id = models.AutoField(primary_key=True)
    SystemParameterName = models.CharField( max_length=30, blank=True, null=True)
    SystemParameterValue = models.CharField( max_length=30, blank=True, null=True)
    SystemParameterUpdatedOn = models.IntegerField( blank=True, null=True) 
    SystemParameterActiveYN = models.IntegerField(db_comment="0 for Not Active, 1 for Active")
    SystemParameterUpdatedByUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True)

    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblSystemParameters_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblSystemParameters_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblSystemParameters_DeletedBy')
    class Meta:
        
        db_table = 'tblSystemParameters'

        
class tblReferedLink(models.Model):
    ReferedLink_Id = models.AutoField(primary_key=True)
    ReferedByUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True)
    ReferedName = models.CharField( max_length=50, blank=True, null=True)
    ReferedMobileNo = models.CharField( max_length=10, blank=True, null=True)
    ReferedEmail = models.CharField( max_length=100, blank=True, null=True)

    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblReferedLink_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblReferedLink_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblReferedLink_DeletedBy')

    class Meta:
        
        db_table = 'tblReferedLink'

class Rates(models.Model):
    Rate_Id = models.AutoField(primary_key=True)
    Rate_Purchase = models.FloatField(blank=True, null=True)
    Rate_Sales = models.FloatField(blank=True, null=True)
    Rate_UpdatedOn = models.IntegerField( blank=True, null=True)
    Rate_UpdatedByUserid = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True)
    
    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='Rates_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='Rates_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='Rates_DeletedBy')


    class Meta:
        
        db_table = 'Rates'


class tblPromoCode(models.Model):
    PromoCode_Id = models.AutoField(primary_key=True)
    PromoCode = models.CharField( max_length=10, blank=True, null=True)
    PromoCodeType = models.IntegerField(db_comment="1=> Percentage, 2=> Fixed Amount")
    PromoCodeValue = models.FloatField(blank=True, null=True)
    PromoCodeValidFrom = models.IntegerField( blank=True, null=True)
    PromoCodeValidUpTo = models.IntegerField( blank=True, null=True)
    PromoCodeValidFor = models.IntegerField(db_comment="0=>Invalid, 1=> All, 2=> All ChannelPartner, 3=> All Members, 4=>Specified ChannelPartner, 4=> Specified Members")
    PromoCodeValidCount = models.IntegerField( blank=True, null=True)
    PromoCodeUsageCount = models.IntegerField( blank=True, null=True)
    PromoCodeStatus = models.IntegerField(db_comment="0=> Unpublished, 1=>Active, 2=> Expired, 3=> Utilized, 4=> Deactive")
    PromoCode_CreatedByUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True)
    PromoCodeCreatedOn = models.IntegerField( blank=True, null=True)
    PromoCodeBannerImagePath = models.CharField( max_length=100, blank=True, null=True)
    
    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblPromoCode_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblPromoCode_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblPromoCode_DeletedBy')
    
    class Meta:
        
        db_table = 'tblPromoCode'


class tblPromoCodeUsages(models.Model):
    PromoCodeusage_Id = models.AutoField(primary_key=True)
    PromoCodeId = models.ForeignKey(tblPromoCode, on_delete=models.SET_NULL, null=True)
    PromoCodeUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True)
    PromoCodeUsageOn = models.IntegerField( blank=True, null=True)
    PromoCodeUsageStatus = models.IntegerField(db_comment="1:Accepted 2: Rejected")
    
    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblPromoCodeUsages_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblPromoCodeUsages_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblPromoCodeUsages_DeletedBy')

    class Meta:
        
        db_table = 'tblPromoCodeUsages'


class tblNomineeDetails(models.Model):
    Nominee_Id = models.AutoField(primary_key=True)
    NomieeForUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True)
    NomineeForAccountId = models.IntegerField( blank=True, null=True)
    NomieeForAccountType = models.IntegerField(db_comment="1: Booking, 2: Deposite")
    NomineeFirstName = models.CharField( max_length=50, blank=True, null=True)
    NomieeLastname = models.CharField( max_length=50, blank=True, null=True)
    NomieeMobileNo = models.CharField( max_length=10, blank=True, null=True)
    NomieeEmail = models.CharField( max_length=100, blank=True, null=True)
    NomieeRelation = models.IntegerField(db_comment="1: Wife, 2: Mother, 3: Father, 4: Daughter ,5: Son ,6: Brother, 7: Sister ,8: Friend, 9: SecondRelative,  10: Other")
    NomieeDateofBirth = models.IntegerField( blank=True, null=True)
    NomieeIsMinorYN = models.IntegerField(db_comment="0: Not Minor 1: Minor")
    NomieeStatus = models.IntegerField(db_comment="0: Added, 1: Approved, 2: Rejected")

    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblNomineeDetails_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblNomineeDetails_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblNomineeDetails_DeletedBy')

    class Meta:
        
        db_table = 'tblNomineeDetails'


class tblMatuniryRateChart(models.Model):
    RateChart_Id = models.AutoField(primary_key=True)
    RateChartStartValue = models.IntegerField( blank=True, null=True)
    RateChartEndValue = models.IntegerField( blank=True, null=True)
    RateChartBankYesValue = models.IntegerField( blank=True, null=True)
    RateChartBankNoValue = models.IntegerField( blank=True, null=True)
    
    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblMatuniryRateChart_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblMatuniryRateChart_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblMatuniryRateChart_DeletedBy')

    class Meta:
        
        db_table = 'tblMatuniryRateChart'


class tblGoldBookingDiscountChart(models.Model):
    DiscountChart_Id = models.AutoField(primary_key=True)
    DiscountChartTennueValue = models.IntegerField( blank=True, null=True)
    DiscountChartQuantity = models.IntegerField( blank=True, null=True)
    DiscountChartAmount = models.IntegerField( blank=True, null=True)
    DiscountChartUpdatedOn = models.IntegerField( blank=True, null=True)
    DicsountChartUpdatedByUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True)
    
    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblGoldBookingDiscountChart_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblGoldBookingDiscountChart_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblGoldBookingDiscountChart_DeletedBy')


    class Meta:
        
        db_table = 'tblGoldBookingDiscountChart'
        

class tblDepositDocuments(models.Model):
    DepositDocument_Id = models.AutoField(primary_key=True)
    DepositDocumentAccountId = models.IntegerField( blank=True, null=True)
    DepositUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True)
    DepositDocumentURL = models.CharField( max_length=100, blank=True, null=True)
    DepositDocumentAddedOn = models.IntegerField( blank=True, null=True)
    
    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblDepositDocuments_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblDepositDocuments_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblDepositDocuments_DeletedBy')


    class Meta:
        
        db_table = 'tblDepositDocuments'

        
class tblChannelPartnerRequests(models.Model):
    CPRequest_Id = models.AutoField(primary_key=True)
    CPUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True)
    CPStatus = models.IntegerField(db_comment="1: Requested ,2: Approved")
    CPRequestOn = models.IntegerField( blank=True, null=True)
    CPRequestAdminUpdatedOn = models.IntegerField( blank=True, null=True)
    
    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblChannelPartnerRequests_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblChannelPartnerRequests_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblChannelPartnerRequests_DeletedBy')

    class Meta:
        
        db_table = 'tblChannelPartnerRequests'

        
class tblChannelPartnerSlabs(models.Model):
    CPS_Id = models.AutoField(primary_key=True)
    CPSLimitStart = models.IntegerField( blank=True, null=True)
    CPSLimitEnd = models.IntegerField( blank=True, null=True)
    CPSMethod = models.IntegerField( blank=True, null=True)
    CPSCommissionType = models.IntegerField(db_comment="1: Percentage ,2: Fixed")
    CPSCommisionValue = models.IntegerField( blank=True, null=True)
    CPSCommisionAddedOn = models.IntegerField( blank=True, null=True)
    CPSCommissionUpdatedon = models.IntegerField( blank=True, null=True)
    CPSCommissionAddedByUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='added_channel_partner_slabs')
    CPSCommissionUpdatedByUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='updated_channel_partner_slabs')
    
    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblChannelPartnerSlabs_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblChannelPartnerSlabs_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblChannelPartnerSlabs_DeletedBy')
    class Meta:
        
        db_table = 'tblChannelPartnerSlabs'

class tblChannelPartnerPayouts(models.Model):
    CPP_Id = models.AutoField(primary_key=True)
    CPPUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='CPPUserId')
    CPPPayoutId = models.CharField( max_length=10, blank=True, null=True)
    CPPGold = models.IntegerField( blank=True, null=True)
    CPPPaidAmount = models.FloatField(blank=True, null=True)
    CPPForMonthYear = models.IntegerField( blank=True, null=True)
    CPPPayoutRemark = models.CharField( max_length=255, blank=True, null=True)
    CPPPayoutStatus = models.IntegerField(db_comment="1: Percentage ,2: Fixed")
    CPPPayoutApprovedByUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='CPPPayoutApprovedByUserId')
    
    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblChannelPartnerPayouts_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblChannelPartnerPayouts_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblChannelPartnerPayouts_DeletedBy')
    class Meta:
        
        db_table = 'tblChannelPartnerPayouts'

class tblBankDetails(models.Model):
    BankDetails_Id = models.AutoField(primary_key=True)
    BankDetails_UserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='BankDetails_UserId')
    BankDetailsName = models.CharField( max_length=100, blank=True, null=True)
    BankDetailsBankName = models.CharField( max_length=100, blank=True, null=True)
    BankDetailsAccountNo = models.CharField( max_length=100, blank=True, null=True)
    BankDetailsIFSC = models.CharField( max_length=100, blank=True, null=True)
    BankDetailsBranch = models.CharField( max_length=100, blank=True, null=True)
    BankDetailsAccountType = models.IntegerField(db_comment="1: Saving 2: Current")
    BankDetailsStatus =  models.IntegerField(db_comment="0: Added, 1: Approved 2: Rejected")
    BankDetailsAddedOn = models.IntegerField( blank=True, null=True)
    BankDetailsAddedByUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='BankDetailsAddedByUserId')
    BankDetailsUpdatedOn = models.IntegerField( blank=True, null=True)
    BankDetailsUpdatedByUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='BankDetailsUpdatedByUserId')
    
    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblBankDetails_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblBankDetails_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblBankDetails_DeletedBy')
    class Meta:
        
        db_table = 'tblBankDetails'

        
class tblGoldBookingDetails(models.Model):
    GBAccountId = models.AutoField(primary_key=True)
    GBAccountDisplayId = models.CharField( max_length=10, blank=True, null=True)
    GBUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='GBUserId')
    GBRate = models.FloatField(blank=True, null=True)
    GBWeight = models.FloatField(blank=True, null=True)
    GBTennure = models.IntegerField( blank=True, null=True)
    GBProcessinChargesApplicable = models.FloatField(blank=True, null=True)
    GBProcessingChargeDisocunt = models.FloatField(blank=True, null=True)
    GBProcessingCharge = models.FloatField(blank=True, null=True)
    GBProcessingChargeGST = models.FloatField(blank=True, null=True)
    GBProcessingChargePayable = models.FloatField(blank=True, null=True)
    GBBookingChargesApplicable = models.FloatField(blank=True, null=True)
    GBBookingChargeDisocunt = models.FloatField(blank=True, null=True)
    GBBookingCharge = models.FloatField(blank=True, null=True)
    GBBookingChargeGST = models.FloatField(blank=True, null=True)
    GBBookingChargePayable = models.FloatField(blank=True, null=True)
    GBPromoCodeId = models.ForeignKey(tblPromoCode, on_delete=models.SET_NULL, null=True, related_name='GBPromoCodeId')
    GBDownPayment = models.FloatField(blank=True, null=True)
    GBFixTennure = models.IntegerField(db_comment="0: No 1: Yes")
    GBFixTennureDiscount = models.FloatField(blank=True, null=True)
    GBBookingAmount = models.FloatField(blank=True, null=True)
    GBMonthlyInstallment = models.FloatField(blank=True, null=True)
    GBAccountStatus = models.IntegerField(db_comment="0: Added 1: Approved 2: Closed 3: Cancelled 4: Rejected")
    GDRStatusByUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='GDRStatusByUserId')
    GDRStatusOn = models.IntegerField( blank=True, null=True)
    GBChannelPartnerUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='GBChannelPartnerUserId')
    
    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblGoldBookingDetails_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblGoldBookingDetails_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblGoldBookingDetails_DeletedBy')
    class Meta:
        
        db_table = 'tblGoldBookingDetails'


class tblVendors(models.Model):
    VendorId = models.AutoField(primary_key=True)
    Vendor_Name = models.CharField( max_length=255, blank=True, null=True)
    VendorLogoPathURL = models.CharField( max_length=255, blank=True, null=True)
    VendorLetterPathURL = models.CharField( max_length=255, blank=True, null=True)
    VendorLogoPathURL = models.CharField( max_length=255, blank=True, null=True)
    VendoradvertisementPathURL = models.CharField( max_length=255, blank=True, null=True)
    VendorStatus = models.IntegerField(db_comment="0: Not Active 1: Active")
    
    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblVendors_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblVendors_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblVendors_DeletedBy')
    class Meta:
        
        db_table = 'tblVendors'

    
class tblGoldDelivery(models.Model):
    GoldDelivery_Id = models.AutoField(primary_key=True)
    GDUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='GDUserId')
    GDAccountId = models.ForeignKey(tblGoldBookingDetails, on_delete=models.SET_NULL, null=True, related_name='GDAccountId')
    GDAccountType = models.IntegerField(db_comment="1: Booking, 2: Deposit")
    GDVendorId = models.ForeignKey(tblVendors, on_delete=models.SET_NULL, null=True, related_name='tblVendors')
    GDTransactionId = models.CharField( max_length=50, blank=True, null=True)
    GDBankDetailsName = models.CharField( max_length=100, blank=True, null=True)
    GDBankDetailsBankName = models.CharField( max_length=100, blank=True, null=True)
    GDBankDetailsAccountNo = models.CharField( max_length=100, blank=True, null=True)
    GDBankDetailsIFSC = models.CharField( max_length=100, blank=True, null=True)
    GDBankDetailsBranch = models.CharField( max_length=100, blank=True, null=True)
    GDBankDetailsAccountType = models.IntegerField(db_comment="1: Saving 2: Current")
    GDAmount = models.FloatField(blank=True, null=True)
    GDComment = models.CharField( max_length=255, blank=True, null=True)
    GDStatus =  models.IntegerField(db_comment="0: Requsted 1: Approved, 2: Rejected")
    GDRequestedOn = models.IntegerField( blank=True, null=True)
    GDApprovedByUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='GDApprovedByUserId')
    GDApprovedOn = models.IntegerField( blank=True, null=True)

    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblGoldDelivery_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblGoldDelivery_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblGoldDelivery_DeletedBy')

    class Meta:
        
        db_table = 'tblGoldDelivery'



class tblUserDevices(models.Model):
    UserDevice_Id = models.AutoField(primary_key=True)
    UserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='UserId')
    UserDeviceDetails = models.CharField( max_length=255, blank=True, null=True)
    UserDeviceToken = models.CharField( max_length=255, blank=True, null=True)
    UserDeviceStatus = models.IntegerField(db_comment="1:Active 2:Deactive 3: Blocked")
    
    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblUserDevices_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblUserDevices_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblUserDevices_DeletedBy')
    class Meta:
        
        db_table = 'tblUserDevices'

        
class tblUserDocuments(models.Model):
    UserDocument_Id = models.AutoField(primary_key=True)
    UserDocumentType = models.IntegerField(db_comment="1: Profile, 2: PAN, 3: Aadhar, 4: Address")
    UserDocumentURL = models.CharField( max_length=255, blank=True, null=True)
    UserDocumentBackURL = models.CharField( max_length=255, blank=True, null=True)
    
    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblUserDocuments_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblUserDocuments_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblUserDocuments_DeletedBy')
    class Meta:
        
        db_table = 'tblUserDocuments'
        
class tblUserActions(models.Model):
    UserAction_Id = models.AutoField(primary_key=True)
    UserActionUserId = models.CharField( max_length=255, blank=True, null=True)
    UserActionFor = models.CharField( max_length=255, blank=True, null=True)
    UserActionOn = models.IntegerField( blank=True, null=True)
    UserActionRequestData = models.CharField( max_length=255, blank=True, null=True)
    UserActionResponseData = models.CharField( max_length=255, blank=True, null=True)

    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblUserActions_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblUserActions_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblUserActions_DeletedBy')
    class Meta:
        
        db_table = 'tblUserActions'

    
class tblGoldDepositeRequests(models.Model):
    GDRAccountId = models.AutoField(primary_key=True)
    GDRAccountDisplayId = models.CharField( max_length=10, blank=True, null=True)
    GDRUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='GDRUserId')
    GDRVendorId = models.ForeignKey(tblVendors, on_delete=models.SET_NULL, null=True, related_name='GDRVendorId')
    GDRChannelPartherId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='GDRChannelPartherId')
    GDRDepositeGold = models.FloatField(blank=True, null=True)
    GDRProcessingChargeApplicable = models.FloatField(blank=True, null=True)
    GDRProcessingChargeDisocunt = models.FloatField(blank=True, null=True)
    GDRProcessingCharge = models.FloatField(blank=True, null=True)
    GDRProcessingChargeGST = models.FloatField(blank=True, null=True)
    GDRProcessingChargePayable = models.FloatField(blank=True, null=True)
    GDRPromoCodeId = models.ForeignKey(tblPromoCode, on_delete=models.SET_NULL, null=True, related_name='GDRPromoCodeId')
    GDRTennure = models.IntegerField( blank=True, null=True)
    GDRGoldRate = models.FloatField(blank=True, null=True)
    GDRGoldAmount = models.FloatField(blank=True, null=True)
    GDRStatus = models.IntegerField(db_comment="0: Deposited, 1: Approved, 2: Closed, 3: Canceled, 4: Rejected")
    GDRStatusByUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='gold_deposite_requests_status_user')
    GDRStatusOn = models.IntegerField( blank=True, null=True)
    GDRMaturityWeight = models.FloatField(blank=True, null=True)
    GDRMaturityDate = models.IntegerField( blank=True, null=True)
    GDRBankGuranteeYN = models.IntegerField(db_comment="1: Yes 0: No")
    GDRRemarks = models.CharField( max_length=255, blank=True, null=True)
    
    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblGoldDepositeRequests_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblGoldDepositeRequests_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblGoldDepositeRequests_DeletedBy')
    
    class Meta:
        
        db_table = 'tblGoldDepositeRequests'


    
class tblGoldBookingTransactions(models.Model):
    GBT_Id = models.AutoField(primary_key=True)
    GBT_AccountId = models.ForeignKey(tblGoldBookingDetails, on_delete=models.SET_NULL, null=True, related_name='GBT_AccountId')
    GBTUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='GBTUserId')
    GBTInstallmentAmount = models.FloatField(blank=True, null=True)
    GBTPeriod = models.IntegerField( blank=True, null=True)
    GBTCreditAmount = models.FloatField(blank=True, null=True)
    GBTRemaining_Amount = models.FloatField(blank=True, null=True)
    GBTDebitAmount = models.FloatField(blank=True, null=True)
    GBTComment = models.CharField( max_length=255, blank=True, null=True)
    GBTEntryType = models.IntegerField(db_comment="1: Installment, 2: Credit, 3: Debit")
    GBTTransactionId = models.CharField( max_length=255, blank=True, null=True)
    GBTWalletPay = models.IntegerField(db_comment="0: No, 1: Yes")
    GBTPaymentMethod = models.IntegerField(db_comment="1: Cash, 2: Cheque, 3: BankTransfer, 4: UPI")
    GBTPaymentDetails = models.CharField( max_length=255, blank=True, null=True)
    GBTTransactionOn = models.FloatField(blank=True, null=True)
    GBTStatus = models.IntegerField(db_comment="0:Inserted 1: Paid 2: Approved 3: Rejected 4: Failed")
    GBTStatusOn = models.IntegerField( blank=True, null=True)
    GBTStatusByUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='GBTStatusByUserId')
    
    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblGoldBookingTransactions_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblGoldBookingTransactions_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblGoldBookingTransactions_DeletedBy')

    class Meta:
        
        db_table = 'tblGoldBookingTransactions'


class tblLoanRequests(models.Model):
    LoanRequestId = models.AutoField(primary_key=True)
    LRUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='LRUser_Id')
    LRAmount = models.FloatField(blank=True, null=True)
    LRComment = models.CharField( max_length=255, blank=True, null=True)
    LRAdminRemark = models.CharField( max_length=255, blank=True, null=True)
    LRAdminStatus = models.IntegerField( blank=True, null=True)
    
    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblLoanRequests_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblLoanRequests_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblLoanRequests_DeletedBy')
    class Meta:
        
        db_table = 'tblLoanRequests'
    
class tblUserLoanDetails(models.Model):
    UserLoan_Id = models.AutoField(primary_key=True)
    LRUserId = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='LRUserId')
    LRTransactionId = models.CharField( max_length=255, blank=True, null=True)
    LRAmount = models.FloatField(blank=True, null=True)
    LRStatus = models.IntegerField( blank=True, null=True)
    LRStatusOn = models.IntegerField( blank=True, null=True)
    LRComment = models.CharField( max_length=255, blank=True, null=True)
    LRAdminRemark = models.CharField( max_length=255, blank=True, null=True)
    LRPaymentMethod = models.IntegerField(db_comment="1: Cash, 2: Cheque, 3: BankTransfer, 4: UPI")
    LRPaymentDetails= models.CharField( max_length=255, blank=True, null=True)
    LRTransactionDetails = models.CharField( max_length=30, blank=True, null=True)
    LRTransactionOn = models.IntegerField( blank=True, null=True)
    
    CreatedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblUserLoanDetails_CreatedBy')
    CreatedOn = models.IntegerField( blank=True, null=True)
    LastModifiedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblUserLoanDetails_LastModifiedBy')
    LastModifiedOn = models.IntegerField( blank=True, null=True)
    IsDeleted = models.IntegerField(default=0)
    DeletedOn = models.IntegerField( blank=True, null=True)
    DeletedBy = models.ForeignKey(tblUsers, on_delete=models.SET_NULL, null=True, related_name='tblUserLoanDetails_DeletedBy')

    class Meta:
        
        db_table = 'tblUserLoanDetails'
