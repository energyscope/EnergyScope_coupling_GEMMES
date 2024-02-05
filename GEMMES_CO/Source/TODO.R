FISIM = 0.1#AG: to be constructed
DIVb_w  = 0 #AG: tocheck
varsigmafdi =  0.002 #varsigma0 + varsigma1*(Xr_0*p_0)/(GDP/en)#FDI to foreign GDP ratio #AG: hardcoded value

mpc1= 1- lambda_l0/(1+exp(-lambda_l1*(0.09 + idep - pDot/p))) #Marginal propensity to consume out income #AG: hardcoded value
mpc2= 1- lambda_w0/(1+exp(-lambda_w1*(0.09 + idep - pDot/p)))  #Marginal propensity to consume out wealth #AG: hardcoded value

idepcb = 0.102 #TODO AG define equation

Bg_f=254.865
Bg_w=83.986

#Other flows
Oth_f=1#AG:todo
Oth_b=5#AG:todo
Oth_g=7#AG:todo
Oth_hh=21#AG:todo
Oth_w=8#AG:todo


D_f_dot = eta_df*F_f#AG: hardcoded value 9.972422415/200.9664
Dfx_f_dot = eta_dfxf*Lfx_fb_dot
Ld_f_dot = TFN_F - Lfx_fb_dot*en - Lfx_fw_dot*en - FDI_f*en
Lfx_fb_dot =  eta_lfxfb*(F_f/en)#AG: TODO
Lfx_fw_dot = eta_lfxfw*(F_f/en)#AG: TODO

D_g_dot = theta_dg*TR #Deposits accumulation by the Government ->AG: check this equation
Dcb_g_dot = theta_dgcb*TR#AG: todo
Dfx_g_dot = theta_dfxg*TR#AG: todo

Rfxb_dot = Dfx_f_dot #FX no-open position condition
Dfx_b_dot = eta_dxfb*Dfx_f_dot #AG:TODO

I_h = 1*(I_hTar-I_h)

en = 0.25*((Dfx-Sfx)/Sfx)*en #Change in nominal exchange rate #AG: hardcoded value
ene = 0.5*(en-ene)  #Change in expected nominal exchange rate #AG: hardcoded value
