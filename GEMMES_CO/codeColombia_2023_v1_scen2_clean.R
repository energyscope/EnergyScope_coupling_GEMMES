##intermediate variables  

#NFC
gk = (ikf + FDIgreen/pk)/kf - deltaf #(*Real*)
yp = ye + ivd# (*Total production Real *)
ivd = betaivd*(vd - v)#(*Desired investment in inventories #Real *)

vd = alphav*ye #(*Desired inventories #Real *)
ypd = yp - im # (*Domestic production (including taxes on products) #Real *)
# u = ypd/(kf*prk)# (*Utilisation rate of capital #Real *)
# Yd = Con + IC + Ik + X #(*Aggregate demand Nominal *)
#ADDED HERE TRANS
Yd = Con + IC + Ik + Iktr + X #(*Aggregate demand Nominal *)

# Ydreal = Con/pc + IC/pi + Ik/pk + X/px#(*X/px#*)(*Aggregate demand,real *)
#ADDED HERE TRANS
yd = Con/pc + IC/pi + Ik/pk + ikftr + X/px#(*X/px#*)(*Aggregate demand,real *)
gdp = Con/pc + Ik/pk + ikftr + x - im
Con = Ch + Cg# (*Total consumption Nominal *)
IC = pi*(icf + icg + icb) #(*Total Intermediate consumption Nominal *)
icf = lambdaicf*yp#(*Real intermediate consumption in NFCs *)
#ADDED HERE TRANS
# ICrf = betaicftr*Ypr#(*Real intermediate consumption in NFCs *)
#What kind of dynamics: something dependent on capital accumulation?

Ik = pk*ikf + Ikh + Ikb + Ikg + FDIgreen# (*Total investment Nominal*)
# ikfTar = (kappa0 + kappa1*(rf - pdot/p) + kappa2*u)*kf#(*Investment Real*)
ikfTar = (kappa0 + kappa1*(rf - pdot/p))*kf#(*Investment Real*)

#ADDED HERE TRANS
Iktr = ikftr*pktr
ikftr = (1/(1.0 + exp(-elastScen*(t - initScen))))*(parmScen*K_0)

# IM = sigmamc*(Con/pc) + sigmamic*(IC/pi) + sigmamk*(Ik/pk) #(*Real imports*)
#ADDED HERE TRANS
im = sigmamc*(Con/pc) + sigmamic*(IC/pi) + sigmamk*(Ik/pk) + sigmamktr*Iktr/pk #(*Real imports*)

sigmamcTar = sigmapcVar*(p/(pw*en*(1 + taum)))^epsilon1c + sigmaac*(aw/a)^epsilon2c #
sigmamicTar = sigmapicVar*(p/(pw*en*(1 + taum)))^epsilon1ic + sigmaaic*(aw/a)^epsilon2ic #
sigmamkTar = sigmapkVar*(p/(pw*en*(1 + taum)))^epsilon1k + sigmaak*(aw/a)^epsilon2k #

sigmapcVar = (1/(1 + exp(sigmamSpeed*t-sigmamInit)))*(sigmapc - sigmapc*sigmapcNew) +  sigmapc*sigmapcNew#  \
sigmapicVar = (1/(1 + exp(sigmamSpeed*t-sigmamInit)))*(sigmapic - sigmapic*sigmapicNew) +  sigmapic*sigmapicNew#  \
sigmapkVar = (1/(1 + exp(sigmamSpeed*t-sigmamInit)))*(sigmapk - sigmapk*sigmapkNew) +  sigmapk*sigmapkNew#  \

#ADDED HERE TRANS
sigmamktrTar = 0.58133 + sigmaaktr*(awgr/agr)^epsilon2ktr

IM = im*pw*en #(*Imports,nominal *)
pm = pw*en# (*Import price, domestic currency*)
er = pw*en/p #(*Real exchange rate *)
X = xrO*pO*en + sigmaxn*GDPw*pwx*en  #(*Total exports,nominal *)
px = X/(xrO + sigmaxn*GDPw) #(*To Check *)
x=X/px
# sigmaxnTar = sigmaxnp*(pwx*en/p)^epsilonxn1 + sigmaxn1*((a/aw)^epsilonxn2) #(*Target propensity to export *)
#ADDED HERE TRANS
sigmaxnTar = sigmaxnpVar*(pwx*en/(p*(1+tauCBAM)))^epsilonxn1 + sigmaxna*((a/aw)^epsilonxn2) #(*Target propensity to export *)
sigmaxnpVar = (1/(1 + exp(sigmaxnSpeed*t-sigmaxnInit)))*(sigmaxnp - sigmaxnp*sigmaxnpNew) +  sigmaxnp*sigmaxnpNew#  \
tauCBAM = tauCBAM0*(kftr/kf)^tauCBAM1

pd = (1 + mu)*huc# (*Desired production price level *)
mu = mu0 - mu1*(v/ye - alphav)# (*Mark-up *)
uc = ((1 + thetawf)*Wf*Lf + pi*icf + tauyf*p*ypd)/ypd# (*Unitary cost *)

# pc = (p*(1 - sigmamc) + pw*en*(1 + taum)*sigmamc)*(1 + tauvat + tauothc)#
pc = (p*(1 - sigmamc) + pw*en*(1 + taum)*sigmamc)*(1 + tauvat + tauothc + tauothctrPub)#
tauothctrPub = shrTax*pubfin*(1-shrIC)*ikftr*pktr/Con #This is the public sector paying for it via carbon tax
pi = (p*(1 - sigmamic) + pw*en*(1 + taum)*sigmamic)*(1 + tauothi + tauothitr + tauothitrPub)#
tauothitr = (1-pubfin)*ikftr*pktr/((p*(1 - sigmamic) + pw*en*(1 + taum)*sigmamic)*(1 + tauothi)*icf) #This is the private sector pays all of it
tauothitrPub = shrTax*pubfin*shrIC*ikftr*pktr/((p*(1 - sigmamic) + pw*en*(1 + taum)*sigmamic)*(1 + tauothi)*icf) #This is the public sector paying for it via carbon tax
# pi = (p*(1 - sigmamic) + pw*en*(1 + taum)*sigmamic)*(1 + tauothi)#
pk = (p*(1 - sigmamk) + pw*en*(1 + taum)*sigmamk)*(1 + tauothk)#
#ADDED HERE TRANS
pktr = (p*(1 - sigmamktr) + pw*en*(1 + taumtr)*sigmamktr)*(1 + tauothktr)#

L = Lf + Lg + Lb #(*Total employment *)
Lf = ypd/a #(*Ypdr/(23.886994*a) #Employment in NFCs *)
#ADDED HERE TRANS
# Lf = Ypdr/(a-atr) #(*Ypdr/(23.886994*a) #Employment in NFCs *)
atr = atr0*(kftr/kf)^atr1

unem = 1 - L/pop# (*Unemployment rate *)

GOSf = Yd - IM - Tm - tauyf*p*ypd - Tp - Tvat - pi*icf - Insf - Comf - (1 + thetawf)*Wf*Lf# (*Gross Operating Surplus in NFCs *)
GOSh = thetaGh*GOSf # (*Gross Operating Surplus redistributed to households *)
GOSg = thetaGg*GOSf #(*Gross Operating Surplus redistributed to the Government *)

MIh = betaHmi*(GOSf)# (*Mixed-income *)
GFf = GOSf - Roy - ildf*Ldf - ilfxb*Lfxfb*en - ilfxfw*Lfxfw*en + idep*(1 - mdf)*Df - (MIh + GOSh + GOSg)# (*Gross profits in NFCs *)
Ff = (1 - tauf)*GFf #(*Net profits in NFCs *)
rf = Ff/(pk*kf)# (*Profit rate in NFCs *)
FNf = Ff - Dfxfdot*en - Dfdot# (*Profits net of deposit accumulation *)

DIVf = (1 - sf)*FNf# (*Dividends paid by NFCs *)
REf = sf*FNf - Othf #(*Retained earnings *)
DIVfw = (ipsilon0w + ipsilon1w*(xrO*pO)/(GDP/en))*DIVf #(*Dividends paid to foreign investors *)
DIVfg = (ipsilon0g + ipsilon1g*(xrO*pO)/(GDP/en))*DIVf#(*Dividends paid to the Government *)
DIVfh = DIVf - DIVfw - DIVfg #(*Dividends paid to households*)

TFNF = pk*ikf - REf#(*Total financing needs in NFCs - Think about these*)
GDP = Ch + Cg + PSg + Ik + Iktr+ X - IM#(*GDP *)
ilfxfw = iwst + rhofx1*premfx#
# Lfxfbdesdot = etalfxfb*(TFNF/en)
# Lfxfwdesdot = etalfxfw*(TFNF/en)

#Banks

Com = Comh + Comf#
Comh = comH*Ldh#
Comf = comF*Ldf#
Ins = Insh + Insf#
Insh = InsH*Krh*pk#
Insf = InsF*kf*pk#
Ybr = Ins + Com#

icb = lambdaicb*Lb #(*FCs' intermediate consumption-real  *)
Ikb = kappaib*Ybr# (*FCs' investment-Nominal *)
STb = (1 - fistg)*ST #(*Social transfers paid by the FCs *)

GOSb = Ybr - pi*icb - tauyb*Ybr - (1 + thetawb)*Wb*Lb# (**)

GFb = ilh*Ldh + ildf*Ldf + ilfxb*Lfxfb*en + ibgdc*Bgb - (idep*Dg + idep*(1 - mdf)*Df + idep*(1 - mdh)*Dh) - ilfxbw*Lfxbw*en + irfxb*Rfxb*en - ip*Ad - pi*icb - tauyb*Ybr - (1 + thetawb)*Wb*Lb - STb + Ins + Com #(*Gross profits in FC's *)
Fb = (1 - taub)*GFb# (*Net profits in FCs *)
OFcar = car*(Ldf + Ldh + Lfxfb*en) #(*Own funds needed to accomplish the leverage \regulation *)
REb = betaof*(OFcar - OFb) #(*Retained earnings in FCs *)
DIVb = Fb - REb - Othb #(*Dividends paid by FCs *)
DIVbh = DIVb# (*FCs' paid to households *)
DIVbw = 0 #(*Assumed to simplify *)

idep = ip - md# (*Target deposit rate *)
idepcb = 0.155# (*TODO AG define equation *)
md = rho0 - rho1/(1 + exp(-rho2*(Ad/Dd-rho3)))# (*Deposit rate mark-down *)
ildf = AFC*(1 + premf)# (*Target interest rate on NFCs' loans *)

AFC = ((idep*Dg + idep*(1 - mdf)*Df + idep*(1 - mdh)*Dh) + ip*Ad)/(Dd + Ad)# 

premfTar = zeta0 + zeta1/(1 + exp(-zeta2*((Ldf + Lfxfb*en + Lfxfw*en)/p*ypd)))# (*NFCs premium on DC loans *)

ilh = ildf*(1 + premh) #(*Target Interest rate on household loans *)

premhTar = chi0 + chi1/(1 + exp(-chi2*(Ldh/YDh)))# (*Target premium on households loans rate *)

ilfxbw = iwst + premfx#

premfx = zetafx0 + zetafx1*(rsk)^zetafx2

# FIP = ((Lfxfw + Lfxbw + Bgfx + Lgfx - Dfxw)*en)/GDP#(* 112 *)#
FIP = ((Lfxfw + Lfxbw + Bgfx + Lgfx + LFXGTr - Dfxw)*en)/GDP#(* 112 *)#

rsk = v1*(IM/(Rfx*en))^v2#v1*FIP^2#  0.01040877/1.103775^2 

# prembTar = ji0 + ji1/(1 + exp(-ji2*(rsk)))#
ilfxb = ilfxbw*(1 + rhofx2*premf)#
# premffxTar = psi0 + psi1/(1 +exp(-psi2*((Lfxfb*en + Lfxfw*en)/(Ldf + Lfxfb*en + Lfxfw*en))))#

Dd = Dg + Dh + Df# (*Total deposits in FCs *)

TFNB = (Ldfdot + Ldhdot + Bgbdot) + Ikb + lr*(Dgdot + Dhdot + Dfdot) - (Dgdot + Dhdot + Dfdot + OFbdot + FDIb) - ITRhdot + (Dfxbdot*en + Lfxfbdot*en - Lfxbwdot*en + Rfxbdot*en) #(*Total financing needs in FCs *)

#Central Bank
ipTar =   iota0 + iota1*(pdot/p - iota2)# (*Target policy rate*)
irfx = iwst + pirfx#(*Interest on FX reserves*)
irfxb = iwst + pirfxb#(*Interest on FX reserves*)
Fcb = ip*Ad + irfx*Rfxcb*en - idepcb*Dcbg# (*Central bank profits*)

#Households
CdhTar = mpc1*YDh + mpc2*(Dh + ITRh) + Ldchdot# (*Target desired consumption-nominal*)

Ch = Cdh# (*Households consumption-nominal*)

LdchTar = thetalh*YDh# (*Consumption credit*)
mpc1 = (1/(1 + exp(-lambdal0*(idep - lambdal1 - pdot/p))))*(mpcUB - mpcLB) + mpcLB#(*Marginal propensity to consume out income #AG:hardcoded value*)

mpc2 = 0# (*Marginal propensity to consume out wealth \#AG:hardcoded value*)
YDh = (1 - tauw)*WL + MIh + ESC + ST - NSC - ilh*Ldh + idep*(1 - mdh)*Dh + DIVfh + DIVbh + Rem*en + GOSh - Insh - Comh + Othhh# (*Households income-nominal*)

WL = Wf*Lf + Wg*Lg + Wb*Lb# (*Wage bill-nominal*)

ESC = thetawf*Wf*Lf + thetawg*Wg*Lg + thetawb*Wb*Lb# (*Employers' social contributions-nominal*)

NSC = ESC + phisc*WL# (*Net social contributions paid by the households-nominal*)

NSCg = NSC# (*Net social contributions paid to the Government-nominal*)
#NSCb = (1 - phiscg)*NSC# (*Net social contributions paid to the FCs-nominal*)
IkhTar = kappahi*YDh# (*Households' investment-nominal*)
kappahi = kappah0 - kappah1*ilh - kappah2*unem# (*Investment to income ratio*)
Sh = YDh - Ch# (*Households savings-nominal*)
TFNH = Ikh - Sh# (*Total financing needs of households-nominal*)
# thetalhTar = thetal0 - thetal1*ilh + thetal2*(yedot/ye)#

#Government
TR = Tt + Roy + GOSg + NSCg + idep*Dg + idepcb*Dcbg + DIVfg - Othg + Fcb# (*Total revenue-nominal *)
Tt = Ti + Tm + Tvat + Tp + Ty# (*Tax revenue *)
Ti = tauw*WL + tauf*GFf + taub*GFb# (*Taxes on income *)

Tm = taum*IM# (*Taxes on imports*)
Tvat = tauvat*Con*((1 - sigmamc)*p + sigmamc*pw*en*(1 + taum))/pc# (*Value-added tax*)
# Tp = tauothc*Con*((1 - sigmamc)*p + sigmamc*pw*en*(1 + taum))/pc + tauothi*IC*((1 - sigmamic)*p + sigmamic*pw*en*(1 + taum))/pi +tauothk*Ik*((1 - sigmamk)*p + sigmamk*pw*en*(1 + taum))/pk# (*Other taxes on products*)
Tp = (tauothc+tauothctrPub)*Con*((1 - sigmamc)*p + sigmamc*pw*en*(1 + taum))/pc + (tauothi+tauothitrPub+tauothitr)*IC*((1 - sigmamic)*p + sigmamic*pw*en*(1 + taum))/pi +tauothk*Ik*((1 - sigmamk)*p + sigmamk*pw*en*(1 + taum))/pk# (*Other taxes on products*)

Ty = tauyf*p*ypd + tauyb*Ybr# (*Taxes on production*)
Roy = taur*(xrO*pO*en)# (*Royalties*)
Gt = Gp + Gip # (*Total Government expenditure*)
# Gp = Gc + (1 + thetawg)*Wg*Lg + pi*ICrg + Gi + STg# (*Government primary expenditure*)
Gp = Gc + (1 + thetawg)*Wg*Lg + pi*icg + Ikg + ikftr*pktr + STg# (*Government primary expenditure*)
# Gip = ibgdc*Bg + ibgfx*Bgfx*en + ilgfx*Lgfx*en# (*Government interest payments*)
Gip = ibgdc*Bg + ibgfx*Bgfx*en + ilgfx*Lgfx*en + LFXGTr*en*iFXtr# (*Government interest payments*)
PSg = (1 + thetawg)*Wg*Lg + pi*icg + deltag*pk*krg# (*Government non-market production*)
Gc = PSg + Cg# (*Government consumption*)
CgTar = fi2*GDP# (*Government market-comnsumption*)
DgTar = fi1*Gt#
DcbgTar = fi5*Gt#
Lg = etag*pop# (*Government employees*)
icg = lambdaicg*Lg# (*Government real intermediate consumption*)
TrDef = ikftr*pktr+LFXGTr*en*iFXtr-tauothctrPub*Con*((1 - sigmamc)*p + sigmamc*pw*en*(1 + taum))/pc-(tauothitrPub+tauothitr)*IC*((1 - sigmamic)*p + sigmamic*pw*en*(1 + taum))/pi
ikgTar = kappag*krg#
IkgTar = ikgTar*pk+scenInv*GDP# (*Government nominal investment*)
# ST = fi3*Wf*(pop - Lg - Lf - Lb)# (*Social transfers received by households*)
ST = fi3*Wf*(pop - Lg - Lf - Lb) + fi4 * Wf*pop
STg = fistg*ST# (*Social transfers paid by the Government*)
FD = Gt - TR - PSg# (*Fiscal deficit*)
TFNG = FD + Dgdot + Dcbgdot + Dfxgdot*en# (*Government financing needs*)
sigmafxTar = sigmaG0 + sigmaG1*CAD# (*Public debt allocation*)
ibgdc = ip + premgd# (*Target interest rate on domestic currency debt*)

# premgTar = phi0 + phi1/(1 + exp(-phi2*((Bg + Bgfx*en + Lgfx*en)/GDP)))# (*Target Government debt premium*)
# premgTar = phi0 + phi1/(1 + exp(-phi2*((Bg + Bgfx*en + Lgfx*en + LFXGTr*en)/GDP)))# (*Target Government debt premium*)

# premgdTar = phi0d + phi1/(1 + exp(-phi2*((Bg + Bgfx*en + Lgfx*en)/GDP)))#(* *)
premgdTar = phi0d + phi1/(1 + exp(-phi2*((Bg + Bgfx*en + Lgfx*en + LFXGTr*en)/GDP)))#(* *)

ibgfx = iwst + rhofx3*premfx#  (*Interest on foreign currency debt*)
ilgfx = (1 - rhofx4)*ibgfx# (*Interest on Gov.foreign currency loans*)

#Rest of World
# NIIP = -(Rfx*en + Dfxw*en - Lfxbw*en - Lfxfw*en - Bgfx*en - Lgfx*en - Bgw)/GDP#  (*International investment position*)
NIIP = -(Rfx*en + Dfxw*en - Lfxbw*en - Lfxfw*en - Bgfx*en - Lgfx*en - LFXGTr*en - Bgw)/GDP#  (*International investment position*)

# NIIPa = -(Rfx*en + Dfxw*en - Lfxbw*en - Lfxfw*en - Bgfx*en - Lgfx*en - Bgw)/GDP#  (*International investment position without equities*)
NIIPa = -(Rfx*en + Dfxw*en - Lfxbw*en - Lfxfw*en - Bgfx*en - Lgfx*en - LFXGTr*en - Bgw)/GDP#  (*International investment position without equities*)

Rem = sigmaRem*GDPw*pw#  (*Remittances*)

CAD = -(TB + IA)/GDP# (*Current account as a percentage of GDP*)

# IA = (Rem + irfx*Rfxcb + irfxb*Rfxb - ibgfx*Bgfx - ilgfx*Lgfx - ilfxbw*Lfxbw - ilfxfw*Lfxfw)*en - DIVfw - DIVbw + Othw - ibgdc*Bgw# (*Income account*)
IA = (Rem + irfx*Rfxcb + irfxb*Rfxb - iFXtr*LFXGTr - ibgfx*Bgfx - ilgfx*Lgfx - ilfxbw*Lfxbw - ilfxfw*Lfxfw)*en - DIVfw - DIVbw + Othw - ibgdc*Bgw# (*Income account*)
TB = X - im*pw*en#  (*Trade balance*)

FDI = varsigmafdi*ikf*pk#  (*Total FDI*)
varsigmafdi = (1/(1 + exp(varsigmafdi1*t-varsigmafdi2)))*(varsigmafdi3 - varsigmafdi3*varsigmafdi4) +  varsigmafdi3*varsigmafdi4#  \
# varsigmafdi = (1/(1 + exp(0.3*t-4)))*(0.3424386 - 0.3424386*0.68) +  0.3424386*0.68#  \
FDIf = zetaff*FDI#  (*FDI in NFCs*)
FDIgreen = shrGreenField*FDIf# (**)
FDIb = (1 - zetaff)*FDI#  (*FDI in FCs*)
FDInonGreen = FDIf - FDIgreen# (**)
# Dfx = IM*pw + ibgfx*Bgfx + ilgfx*Lgfx + ilfxbw*Lfxbw + ilfxfw*Lfxfw + DIVfw/en + DIVbw/en + Rfxbdesdot + Dfxwdot + ibgdc*Bgw/en# (**)
Dfx = im*pw + ibgfx*Bgfx + ilgfx*Lgfx + ilfxbw*Lfxbw + ilfxfw*Lfxfw + iFXtr*LFXGTr + DIVfw/en + DIVbw/en + Rfxbdesdot + Dfxwdot + ibgdc*Bgw/en# (**)
# Sfx = X/en + Rem + Othw/en + irfx*Rfxcb + irfxb*Rfxb + FDI/en + Bgfxdot + Lgfxdot + Lfxfwdot + Lfxbwdot + Bgwdot/en - Rfxcbdot# (**)
Sfx = X/en + Rem + Othw/en + irfx*Rfxcb + irfxb*Rfxb + FDI/en + Bgfxdot + Lgfxdot + Lfxfwdot + Lfxbwdot + LFXGTrdot + don*ikftr*pktr/en + Bgwdot/en - Rfxcbdot# (**)
# iwstTar = alphapw#  (*Short-term external interest rate*)

#Other flows
Othf = nuf*ypd*p# (*AG:todo*)
Othb = nub*ypd*p#(*AG:todo*)
Othg = nug*ypd*p# (*AG:todo*)
Othhh = nuh*ypd*p# (*AG:todo*)
Othw = nuw*ypd*p#                       

#Dot equations
yedot = betay*(yd - ye) + gk*ye# (*Expected sales adjustment *)
vdot = yp - yd# (*Change in actual inventories*)
# uedot = betau*(u - ue)# (*Change in expected utilisation rate of capital*)
kfdot = ikf + FDIgreen/pk - deltaf*kf# (*NFCs' capital stock accumulation*)
kftrdot = ikftr - deltaf*kftr# (*NFCs' capital stock accumulation*)
ikfdot = betaikf*(ikfTar - ikf)# (*NFCs' investment adjustment*)
sigmamcdot = betasigmamc*(sigmamcTar - sigmamc)# (*Adjustment in propensity to import consumption goods*)
sigmamicdot = betasigmamic*(sigmamicTar - sigmamic)# (*Adjustment in propensity to intermediate goods*)
sigmamkdot = betasigmamk*(sigmamkTar - sigmamk)# (*Adjustment in propensity to import investment goods*)

# sigmamcdot = ifelse(sigmamcTar>sigmamc,betasigmamc*(sigmamcTar - sigmamc),speedProp*betasigmamc*(sigmamcTar - sigmamc))# (*Adjustment in propensity to import consumption goods*)
# sigmamicdot = ifelse(sigmamicTar>sigmamic,betasigmamic*(sigmamicTar - sigmamic),speedProp*betasigmamic*(sigmamicTar - sigmamic))# (*Adjustment in propensity to intermediate goods*)
# sigmamkdot = ifelse(sigmamkTar>sigmamk,betasigmamk*(sigmamkTar - sigmamk),speedProp*betasigmamk*(sigmamkTar - sigmamk))# (*Adjustment in propensity to import investment goods*)
sigmamktrdot = betasigmamktr*(sigmamktrTar - sigmamktr)# (*Adjustment in propensity to import investment goods*)
sigmaxndot = betasigmaxn*(sigmaxnTar - sigmaxn)# (*Adjustment in propensity to export*)
# sigmaxndot = ifelse(sigmaxnTar>sigmaxn,speedProp*betasigmaxn*(sigmaxnTar - sigmaxn),betasigmaxn*(sigmaxnTar - sigmaxn))# (*Adjustment in propensity to export*)
hucdot = betahuc*(uc - huc)# (*Adjustment in historical unitary cost*)
pdot = betap*(pd - p)# (*Domestic inflation rate*)
Wfdot = (omegaf0*(adot/a) + omegaf1*(L/pop - omegaf2) + omegaf3*pdot/p)*Wf#(**)

Dfdot = betaDf*(etadf*Wf*Lf*(1 + thetawf) - Df)#(*AG:hardcoded value 9.972422415/200.9664 *)

Lbdot = etab*Lb# (*Employment in FCs*)
Krbdot = Ikb/pk - deltab*Krb# (*FCs' capital stock accumulation*)
Wbdot = (omegab0*(adot/a) + omegab1*pdot/p)*Wb# (*Average in FCs*)

Rfxcbdot = max(sigmaRfxb*im*pw - Rfxcb, 0)#
Rfxbdot = Rfxdot - Rfxcbdot# (*FX no-open position condition*)
Rfxbdesdot = Lfxbwdesdot - Dfxbdot - Lfxfbdot# (*FX no-open position condition*)

Dfxbdot = betadfxb*(etadbfx*Lfxbw - Dfxb)# (*AG:TODO*)

Lfxbwdesdot = (etalxfbw*OFbdot/en + Lfxfbdesdot)# (*FCs' FX loans*)

Lfxbwdot = (1 - ratBFX)*Lfxbwdesdot# (*FCs' FX loans*)

ratFFX = 1/(1.0 + exp(-betariskFFX*(rsk - MPFFX)))*(UBFFX - LBFFX) + LBFFX
ratBFX = 1/(1.0 + exp(-betariskBFX*(rsk - MPBFX)))*(UBBFX - LBBFX) + LBBFX

Lfxfbdesdot = etalfxfb*(TFNF/en)#(*AG:TODO *)
Lfxfbdot = (1 - ratBFX)*Lfxfbdesdot#(*AG:TODO *)
Lfxfwdot = (1 - ratFFX)*etalfxfw*(TFNF/en)#(*AG:TODO *)

Dfxfdot = betaDfx*(etadfxf*(Lfxfb + Lfxfw) - Dfxf)# (**)

Ldfdot = TFNF - Lfxfbdot*en - Lfxfwdot*en - FDInonGreen# 

Addot = max(TFNB, -Ad)# (*Liquidity Advances*)
Bgbdot = Bgdot - Bgwdot#(**)
Rddot = lr*((Dgdot + Dhdot + Dfdot))#(*AG:todo*)
OFbdot = REb# (*Change in own funds*)

premfdot = betapremf*(premfTar - premf)# (*Adjustment in the NFCs' loans premium*)
premhdot = betapremh*(premhTar - premh)# (*Adjustment in the households' loans premium*)
# prembdot = betapremb*(prembTar - premb)#(**)
# premffxdot = betapremffx*(premffxTar - premffx)#(**)
ipdot = betaip*(ipTar - ip)# (*Policy rate adjustment*)


Cdhdot = betacon*(CdhTar - Cdh)# (*Adjustment in desired consumption*)
Krhdot = Ikh/pk - deltah*Krh# (*Households' capital stock accumulation*)
Ikhdot = betaIh*(IkhTar - Ikh)#

Dhdot = Sh - Ikh + Ldhdot - ITRhdot# (*Households deposits accumulation*)
Ldhdot = Ldchdot + Ldihdot# (*Total households loans*)
ITRhdot = zetaitr*WL# (*Technical Insurance Reserves accumulation*)
Ldihdot = thetal3*Ikh# (*Mortgage loans*)
Ldchdot = betaLdch*(LdchTar - Ldch)#


thetalhdot = 0#
Wgdot = (omegag0*(adot/a) + omegag1*pdot/p)*Wg# (*Average wage in the Government*)
Ikgdot = betaIkg*(IkgTar - Ikg)# (*Public investment*)
Cgdot = betaCg*(CgTar - Cg)# (*Public market consumption*)
krgdot = Ikg/pk - deltag*krg #(*Government capital stock accumulation*)

Dgdot = betaDg*(DgTar - Dg)# (*Deposits accumulation by the Government\[Rule]AG:check this equation*)
Dcbgdot = betaDcbg*(DcbgTar - Dcbg)#(*AG:todo*)
Dfxgdot = betaDfxg*(etadfxg*(Lgfx + Bgfx) - Dfxg)#(*AG:todo*)
Bgdot = TFNG - Bgfxdot*en - Lgfxdot*en - LFXGTrdot*en - don*ikftr*pktr/en# (*Government domestic currency debt issuance*)
# Bgdot = TFNG - Bgfxdot*en - Lgfxdot*en# (*Government domestic currency debt issuance*)
Bgfxdot = -zetabgfx*(sigmafx*TB/en)# (*Government Foreign currency debt issuance*)
Bgwdot = -zetabg*TB#(**)
Lgfxdot = -(1 - zetabgfx)*(sigmafx*TB/en)# (*Government Foreign currency loans*)
LFXGTrdot = fxtrshare*(1 - don)*ikftr*pktr/en

# premgdot = betapremg*(premgTar - premg)# (*Adjustment in fthe premium on public debt*)
premgddot = betapremgd*(premgdTar - premgd)# (*Adjustment in fthe premium on public debt*)
# Rfxdot = (TB/en + IA/en + FDI/en + Bgfxdot + Bgwdot/en + Lgfxdot + Lfxfwdot + Lfxbwdot - Dfxwdot)#
Rfxdot = (TB/en + IA/en + FDI/en + Bgfxdot + Bgwdot/en + Lgfxdot + Lfxfwdot + Lfxbwdot + LFXGTrdot + don*ikftr*pktr/en - Dfxwdot)#

Dfxwdot = Dfxfdot + Dfxbdot + Dfxgdot#(**)

endot = betaen*((Dfx - Sfx)/Sfx)# (*Change in nominal exchange rate #AG:hardcoded value*)

adot = alphaa*a# (*Domestic productivity growth rate*)
awdot = alphaw*aw# (*Foreign productivity growth rate*)
agrdot = alphaa*agr# (*Domestic productivity growth rate*)
awgrdot = alphaw*awgr# (*Foreign productivity growth rate*)
pwdot = alphapw*pw# (*Foreign inflation rate*)
pwxdot = alphapw*pwx# 
pOdot = alphapO*pO#(**)
GDPwdot = alphagw*GDPw# (*Foreign real GDP growth rate*)
popdot = alphapop*pop# (*Labour force growth rate*)
# iwstdot = betaiwst*(iwstTar - iwst)#
sigmafxdot = betasigmafx*(sigmafxTar-sigmafx)

##time derivatives

ye = yedot
v = vdot
# ue = uedot
kf = kfdot
kftr = kftrdot

ikf = ikfdot
sigmamc = sigmamcdot

sigmamic = sigmamicdot
sigmamk = sigmamkdot
sigmamktr = sigmamktrdot

sigmaxn = sigmaxndot

huc = hucdot
p = pdot
Wf = Wfdot

Df = Dfdot
Dfxf = Dfxfdot
Lfxfb = Lfxfbdot
Lfxfw = Lfxfwdot
Ldf = Ldfdot

Lb = Lbdot
Krb = Krbdot
Wb = Wbdot

Rfxb = Rfxbdot
Dfxb = Dfxbdot
Lfxbw = Lfxbwdot
Ad = Addot
Bgb = Bgbdot
Rd = Rddot
OFb = OFbdot

premf = premfdot

premh = premhdot
# premb = prembdot
# premffx = premffxdot
ip = ipdot
Cdh = Cdhdot


Krh = Krhdot
Ikh = Ikhdot
Dh = Dhdot



Ldh = Ldhdot
ITRh = ITRhdot
Ldih = Ldihdot
#thetalh = thetalhdot
Wg = Wgdot

Ikg = Ikgdot
Cg = Cgdot
krg = krgdot

Dg = Dgdot
Dcbg = Dcbgdot
Dfxg = Dfxgdot
Bg = Bgdot
Bgfx = Bgfxdot
Bgw = Bgwdot
Lgfx = Lgfxdot
LFXGTr = LFXGTrdot

# premg = premgdot
premgd = premgddot

Rfx = Rfxdot
Dfxw = Dfxwdot
Rfxcb = Rfxcbdot

en = endot

a = adot
aw = awdot
agr = agrdot
awgr = awgrdot

pw = pwdot
pwx = pwxdot
pO = pOdot
GDPw = GDPwdot
pop = popdot
Ldch = Ldchdot

# iwst = iwstdot

sigmafx = sigmafxdot
xrO=-reducXrO*xrO
##initial values 
ye=1674.564
v=127.1373
# ue=0.7554824
kf=2213.6793921781
kftr=0
ikf=104.167738781951
sigmamc=0.11989
sigmamic=0.09466
sigmamk=0.29089
sigmamktr=0.4
sigmaxn=0.001288757
huc=0.714649985328843
p=1.087
Wf=11.443
Df=82.931
Dfxf=16.73778
Lfxfb=21.5441
Lfxfw=97.22792
Ldf=234.187
Lb=0.348
Krb=9.917121116
Wb=47.09
Rfxb=40.27344
Dfxb=11.71839
Lfxbw=69.91541
Ad=8.55
Bgb=254.865
Rd=102.482
OFb=105.95
premf=1.65962
premh=0.44049
# premb=0.01045975
# premffx=0.010342564
ip=0.058
Cdh=686.6039807
Krh=368.88722
Ikh=49.722
Dh=173.869
Ldh=198.497
ITRh=506.068
Ldih=62.111
Wg=29.596
Ikg=36.683
Cg=21.601
krg=498.486630008789
Dg=50.705
Dcbg=7.943
Dfxg=8.599901
Bg=338.851
Bgfx=147.8425
Bgw=83.986
Lgfx=59.73074
LFXGTr=0
# premg=-0.047380243
premgd=0.012
Rfx=171.8851
Dfxw=32.20152
Rfxcb=131.6116
en=1.19513
a=74.45
aw=80
agr=74.45
awgr=80
pw=0.9513
pwx=0.555204468
pO=4.038202828
GDPw=88952.63574
pop=24.404942
Ldch=236.386
sigmafx=0.04
XrO = 19.09267727
##parameters
#NFC Params

betaivd=0.16300412
deltaf=0.04
alphav=0.07831128
prk=0.833333333333333
lambdaicf=0.4063
kappa0=0.027
kappa1=0.5
# kappa2=0
sigmapc=0.129665973681575
sigmapcNew=1
epsilon1c=0.75425
sigmaac=0.00025
epsilon2c=1.5758
sigmapic=0.100863727514328
sigmapicNew=1
epsilon1ic=0.6912
sigmaaic=0.00085
epsilon2ic=2.0637
sigmapk=0.304856100732353
sigmapkNew=1
epsilon1k=0.4454
sigmaak=0.00022
epsilon2k=0.241
sigmamSpeed=0.3
sigmamInit=4
sigmaxnp=0.001428421
sigmaxnpNew=1
sigmaxnSpeed=0.4
sigmaxnInit=5
epsilonxn1=0.6
sigmaxna=0.00025
epsilonxn2=1.3745340223
taum=0.064085801
mu0=0.59143893
mu1=0.01321461
tauvat=0.092728882
tauothc=0
tauothi=0.024434906
tauothk=0.024434906
thetaGh=0.09721126
thetaGg=0.005745633
tauyf=0.0172865778595673
thetawf=0.1642046
betaHmi=0.380038148084672
mdf=0.282092928
tauf=0.1738257
ipsilon0w=0.067902982
ipsilon1w=0
ipsilon0g=0.142296618
ipsilon1g=0
sf=0.460959487668661
rhofx1=6.4

#Banks
comH=0.09065261
comF=0.1365994
InsH=0
InsF=0
lambdaicb=75.1592
kappaib=0.06862745
tauyb=0.03
thetawb=0.1884146
mdh=0.314469636
taub=0.1142567
car=0.2742203
betaof=1
rho0=0.530451
rho1=1
rho2=1
rho3=0.01
zeta0=1.615406
zeta1=0
zeta2=0
chi0=0.44
chi1=0
chi2=0
ji0=0.01045975
ji1=0
ji2=0
psi0=0.01034256
psi1=0
psi2=0
lr=0.1585843
zetafx2=1
zetafx0=0.003
zetafx1=0.700904682321678
v1=0.008543549
v2=2
rhofx2=0.185277

#Central Bank Params
iota0=0.04852755
iota1=2
iota2=0.03
pirfx=-0.003146882
pirfxb=0.01935873

#Households Params
lambdal0=-6
lambdal1=0.013
tauw=0.08398394
phisc=0.01585536
# phiscg=1
kappah0=0.0727037178355884
kappah1=0
kappah2=0
# thetal0=0.321717066621123
# thetal1=0
# thetal2=0
mpcUB=0.9877068
mpcLB=0.87
thetalh=0.321717066621123


#Governement
taur=0.102013522823697
thetawg=0.2721489
deltag=0.035
fi1=0.11209336702978144
fi2=0.0225
etag=0.08703155
lambdaicg=23.17883
kappag=0.07
# fi3=5.04722189217687
fi3=0.504722189217687
fi4=0.3434567
fi5=0.024740401610319002
fistg=0.929015
phi0d=0.012
phi1=0
phi2=0
rhofx4=0.077770133
sigmaG0=0.04
sigmaG1=0
rhofx3=0.887389870407265

#RestofWorld params
sigmaRem=0.0002356039
zetaff=0.7762527
shrGreenField=0.4840946
varsigmafdi1=0.3
varsigmafdi2=4
varsigmafdi3=0.385874414238394
varsigmafdi4=0.68
iwst=0.023175727


#other params
betay=3
betau=1.0009
betasigmamc=0.58575193478
betasigmamic=0.64114086974
betasigmamk=1.77651522362
betasigmaxn=1
betap=0.75
omegaf0=1
omegaf1=0
omegaf2=0.8797
omegaf3=1
etab=0.01
deltab=0.0448
betapremf=0.8507
betapremh=1.2339
betapremb=10.5399
betapremffx=0.5144
omegab0=1
omegab1=1
betaip=0.5
betacon=1
deltah=3.2e-06
betaIh=1
betaLdch=12
omegag0=1
omegag1=1
betaIkg=1
betaCg=1
betapremgd=1
betaen=2.5
alphaa=0.02
alphaw=0.02
alphagw=0.03
alphapop=0.01
alphapw=0.03
betaikf=1
alphapO=0.03
betahuc=15
betaDf=1
etadf=0.35
betaDfx=1
etadfxf=0.14
etalfxfb=0.04
etalfxfw=0.13
ratFFX=0.15
betadfxb=0.8
betaDfxg=1
etadbfx=0.0535
etalxfbw=0.2
zetaitr=0.03468189
thetal3=0.126704476891517
betaDg=0.965
betaDcbg=1
etadfxg=0.0265
zetabg=0.016
zetabgfx=0.6
# betaiwst=1
sigmaRfxb=0.74
UBFFX=1.11879
UBBFX=1.07687
LBFFX=0.029903
LBBFX=0.37229
betariskFFX=30
betariskBFX=30
MPFFX=0.08
MPBFX=0.08
betasigmafx=3
nuf = -0.0003904036
nub = 0.007269213
nug = 0.003295476
nuh = 0.01509832
nuw = 0.00492403



#Transition scenario
don = 0.0
iFXtr = 0.015
K_0=1560.2222 #2019 value
elastScen = 0
initScen = 15
parmScen = 0
sigmaaktr = 0.00044# (double from sigmamk)
epsilon2ktr = 0.241# (same as sigmamk)
taumtr=0.064085801 #Same as other propensities
tauothktr=0.024434906 #Same as other propensities
betasigmamktr = 1.77651522362#
# speedProp=1
reducXrO=-0.03 #Reduction rate of exports of oil in real terms
#Alternative scenario parameters
tauCBAM0=0 #For now -> play with it if change in CBAM
tauCBAM1=1
atr0=0 #For now -> play with it if change with labor intensity
atr1=1
pubfin=0 #Who pays: private=0, public=1
shrTax=0 #share of tax funded public investment
shrIC=0.5 #share of public tax going to IC
fxtrshare=1 #share of fx debt 
scenInv=0
#Check also the initial conditions of agr and awgr
##time
begin = 2019
end = 2050
by = 0.1
