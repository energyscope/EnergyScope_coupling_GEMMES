#ifndef PREPROC_H
#define PREPROC_H

// parameters to define prior to compile time

#define UseParallel 					0
#define UseEventTime 					0
#define UseEventVar 					0
#define ReturnRK4 						3
#define VerboseCMAES			        0

#define ntForPython						331
#define TInitForPython					2019
#define TEndForPython					2052
#define NVForPython                     74
#define NIVForPython                    339
#define VarNamesForPython				{"ye", "v", "kf", "ktr", "ikf", "sigmamc", "sigmamic", "sigmamk", "sigmamktr", "sigmaxn", "huc", "p", "Wf", "Df", "Dfxf", "Lfxfb", "Lfxfw", "Ldf", "Lb", "krb", "Wb", "Rfxb", "Dfxb", "Lfxbw", "Ad", "Bgb", "Rd", "OFb", "premf", "premh", "ip", "Ch", "krh", "Ikh", "Dh", "Ldh", "IPSh", "Ldih", "thetalh", "Wg", "Ikg", "Cg", "krg", "Dg", "Dcbg", "Dfxg", "Bg", "Bgfx", "Bgw", "Lgfx", "Lgfxtr", "Bgtr", "Bgwtr", "Bgbtr", "premgd", "Rfx", "Dfxw", "Rfxcb", "en", "a", "aw", "agr", "awgr", "pw", "pwtr", "pwx", "pO", "pef", "GDPw", "pop", "Ldch", "sigmafx", "xrO", "adj_iktr"}
#define IntermediateVarNamesForPython	{"pkefCO", "pkefM", "pkebCO", "pkebM", "pkegCO", "pkegM", "pkehCO", "pkehM", "ikef", "ikeb", "ikeg", "ikeh", "sigmamkef", "sigmamkeb", "sigmamkeg", "sigmamkeh", "icef", "sigmamicef", "iceb", "sigmamiceb", "iceg", "sigmamiceg", "ceh", "sigmamceh", "pieM", "xef", "CTf", "CTb", "CTg", "CTh", "reducXrO", "iwst", "v1", "iota0", "theta_El_F", "theta_HLTHW_F", "theta_HLTSH_F", "theta_HHT_F", "theta_PC_F", "theta_MF_F", "theta_NE_F", "theta_El_B", "theta_HLTSH_B", "theta_SC_B", "theta_El_G", "theta_HLTSH_G", "theta_SC_G", "theta_El_H", "theta_HLTHW_H", "theta_HLTSH_H", "theta_SC_H", "theta_MP_H", "El_F", "HLTSH_F", "HLTHW_F", "HHT_F", "PC_F", "MF_F", "NE_F", "El_B", "HLTSH_B", "SC_B", "El_G", "HLTSH_G", "SC_G", "El_H", "HLTSH_H", "HLTHW_H", "SC_H", "MP_H", "gk", "yp", "ivd", "vd", "ypd", "Yd", "yd", "Con", "IC", "icf", "Ik", "ikfTar", "kappa0", "Ikftot", "Ikbtot", "Ikgtot", "Ikhtot", "Icftot", "Icbtot", "Icgtot", "lambdaiktr", "iktr", "Iktr", "adj_iktr_tar", "IM", "im", "imkef", "imkeb", "imkeg", "imkeh", "imicef", "imiceb", "imiceg", "imceh", "sigmamcTar", "sigmamicTar", "sigmamkTar", "sigmamktrTar", "sigmapcVar", "sigmapicVar", "sigmapkVar", "X", "x", "sigmaxnTar", "sigmaxnpVar", "tauCBAM", "GDP", "gdp", "pd", "mu", "uc", "pc", "pi", "pk", "px", "pktr", "pkef", "pkeb", "pkeg", "pkeh", "pief", "pieb", "pieg", "pceh", "taugreenic", "taugreenc", "er", "pm", "L", "Lf", "atr", "unem", "GOSf", "GOSh", "GOSg", "MIh", "GFf", "Ff", "FNf", "rf", "DIVf", "DIVfw", "DIVfg", "DIVfh", "REf", "TFNF", "Ybr", "Com", "Comh", "Comf", "Ins", "Insh", "Insf", "icb", "lambdaicb", "Ikb", "STb", "WSCb", "GOSb", "GFb", "Fb", "OFcar", "REb", "DIVb", "DIVbh", "DIVbw", "Dd", "TFNB", "idep", "md", "ildf", "AFC", "premfTar", "ilh", "premhTar", "premfx", "ilfxbw", "ilfxb", "ilfxfw", "ipTar", "irfx", "irfxb", "Fcb", "idepcb", "YDh", "WL", "ESC", "WSC", "ChTar", "Ch_NE_Tar", "mpc1", "mpc2", "LdchTar", "IkhTar", "kappahi", "Sh", "TFNH", "TR", "Tt", "Ti", "Tm", "Tvat", "Tp", "Tgr", "Ty", "Roy", "WSCg", "Gt", "Gp", "Gip", "Gc", "PSg", "CgTar", "Lg", "icg", "lambdaicg", "ikgTar", "IkgTar", "ST", "STg", "FD", "TFNG", "DgTar", "DcbgTar", "sigmafxTar", "ibgdc", "premgdTar", "ibgfx", "ilgfx", "ilgfxtr", "ibgtr", "CAD", "TB", "IA", "Grants", "Rem", "FDI", "varsigmafdi", "FDIf", "FDIgreen", "FDInonGreen", "FDIb", "Dfx", "Sfx", "NIIP", "FIP", "rsk", "Othf", "Othb", "Othg", "Othhh", "Othw", "yedot", "vdot", "ikfdot", "kfdot", "ktrdot", "sigmamcdot", "sigmamicdot", "sigmamkdot", "sigmamktrdot", "sigmaxndot", "hucdot", "pdot", "adot", "agrdot", "popdot", "Wfdot", "Dfdot", "Dfxfdot", "Lfxfbdesdot", "Lfxfbdot", "Lfxfwdot", "ratFFX", "Ldfdot", "krbdot", "Lbdot", "Wbdot", "Rfxbdesdot", "Rfxbdot", "Dfxbdot", "Lfxbwdesdot", "Lfxbwdot", "ratBFX", "Bgbdot", "Bgbtrdot", "Rddot", "OFbdot", "Addot", "premfdot", "premhdot", "Rfxcbdot", "ipdot", "Chdot", "Ikhdot", "krhdot", "Ldhdot", "Ldihdot", "Ldchdot", "thetalhdot", "IPShdot", "Dhdot", "Cgdot", "Ikgdot", "krgdot", "Wgdot", "Dgdot", "Dcbgdot", "Dfxgdot", "sigmafxdot", "Bgfxdot", "Lgfxdot", "Lgfxtrdot", "Bgtrdot", "Bgdot", "premgddot", "Bgwdot", "Bgwtrdot", "Rfxdot", "Dfxwdot", "endot", "awdot", "awgrdot", "pwdot", "pwtrdot", "pwxdot", "pOdot", "pefdot", "GDPwdot"}
#define ParmsNamesForPython				{"betay", "alphav", "betaivd", "lambdaicf", "kappa01", "kappa02", "kappa03", "kappa04", "kappa05", "kappa1", "betaikf", "deltaf", "sigmapc", "sigmapcNew", "epsilon1c", "sigmaac", "epsilon2c", "betasigmamc", "sigmapic", "sigmapicNew", "epsilon1ic", "sigmaaic", "epsilon2ic", "betasigmamic", "sigmapk", "sigmapkNew", "epsilon1k", "sigmaak", "epsilon2k", "betasigmamk", "sigmamSpeed", "sigmamInit", "sigmaxnp", "epsilonxn1", "sigmaxna", "epsilonxn2", "betasigmaxn", "sigmaxnpNew", "sigmaxnSpeed", "sigmaxnInit", "mu0", "mu1", "betahuc", "betap", "thetaGh", "thetaGg", "betaHmi", "omegaf0", "omegaf1", "omegaf2", "omegaf3", "thetawf", "alphaa", "alphapop", "ipsilon0w", "ipsilon1w", "ipsilon0g", "ipsilon1g", "sf", "etadf", "betaDf", "etadfxf", "betaDfx", "etalfxfb", "etalfxfw", "betariskFFX", "UBFFX", "LBFFX", "MPFFX", "comH", "comF", "InsH", "InsF", "lambdaicb1", "lambdaicb2", "lambdaicb3", "lambdaicb4", "lambdaicb5", "etab", "kappaib", "deltab", "omegab0", "omegab1", "thetawb", "car", "betaof", "etadbfx", "betadfxb", "rho0", "rho1", "rho2", "rho3", "mdf", "mdh", "zeta0", "zeta1", "zeta2", "betapremf", "chi0", "chi1", "chi2", "betapremh", "zetafx2", "zetafx0", "zetafx1", "rhofx1", "rhofx2", "etalxfbw", "betariskBFX", "UBBFX", "LBBFX", "MPBFX", "lr", "iota1", "iota2", "betaip", "pirfx", "pirfxb", "sigmaRfxb", "phisc", "betacon", "lambdal0", "lambdal1", "mpcUB", "mpcLB", "betaLdch", "thetal3", "kappah0", "kappah1", "kappah2", "betaIh", "deltah", "zetaitr", "tauf", "taub", "tauw", "taum", "tauvat", "tauothc", "tauothi", "tauothk", "tauyf", "tauyb", "taur", "phiscg", "omegag0", "omegag1", "thetawg", "etag", "lambdaicg1", "lambdaicg2", "lambdaicg3", "lambdaicg4", "lambdaicg5", "kappag", "deltag", "betaIkg", "fi2", "betaCg", "fi3", "fi4", "fistg", "fi1", "betaDg", "fi5", "betaDcbg", "etadfxg", "betaDfxg", "sigmaG0", "sigmaG1", "betasigmafx", "zetabgfx", "phi0d", "phi1", "phi2", "betapremgd", "rhofx3", "rhofx4", "sigmaRem", "varsigmafdi1", "varsigmafdi2", "varsigmafdi3", "varsigmafdi4", "zetaff", "shrGreenField", "v2", "zetabg", "betaen", "alphaw", "alphagw", "alphapw", "alphapwtr", "alphapO", "alphapef", "nuf", "nub", "nug", "nuh", "nuw", "shrDon", "shrGrTax", "shrGrIC", "shrGrL", "shrGrLFx", "shrGrBw", "md_lgtr", "md_bgtr", "K_0", "lambdatr0", "lambdatr1", "lambdatr2", "taumtr", "tauothktr", "betasigmamktr", "lambdatr0_adj", "lambdatr1_adj", "lambdatr2_adj", "tauCBAM0", "tauCBAM1", "sigmamktr0", "sigmaaktr", "epsilon2ktr", "atr0", "atr1", "scenInv"}
#define YInitForPython					{1674.564, 127.1373, 2213.6793921781, 0, 96.69562, 0.11989, 0.09466, 0.29089, 0.5741354, 0.001288757, 0.714649985328843, 1.087, 11.443, 82.931, 16.73778, 21.5441, 97.22792, 234.187, 0.348, 9.917121116, 47.09, 40.27344, 11.71839, 69.91541, 8.55, 254.865, 102.482, 105.95, 1.65962, 0.44049, 0.058, 681.7516, 368.88722, 46.8976, 173.869, 198.497, 506.068, 62.111, 0.321717066621123, 29.596, 33.62179, 21.601, 498.486630008789, 50.705, 7.943, 8.599901, 338.851, 147.8425, 83.986, 59.73074, 0, 0, 0, 0, 0.012, 171.8851, 32.20152, 131.6116, 1.19513, 74.45, 80, 74.45, 80, 0.9513, 0.9513, 0.555204468, 4.038202828, 0.9513, 88952.63574, 24.404942, 236.386, 0.04, 19.09267727, 0}
#define ParmsForPython					{3, 0.07831128, 0.16300412, 0.401234785, 0.2, 1, 0.0370265, 1, -0.005653612, 0.5, 1, 0.04, 0.129665973681575, 1, 0.75425, 0.00025, 1.5758, 0.58575193478, 0.100863727514328, 1, 0.6912, 0.00085, 2.0637, 0.64114086974, 0.304856100732353, 1, 0.4454, 0.00022, 0.241, 1.77651522362, 0.3, 4, 0.001428421, 0.6, 0.00025, 1.3745340223, 1, 1.2, 0.48, 5, 0.59143893, 0.01321461, 15, 0.75, 0.09721126, 0.005745633, 0.380038148084672, 1, 0, 0.8797, 1, 0.1642046, 0.02, 0.01, 0.02, 1.095614749, 0.019036217, 0.848266913, 0.460959487668661, 0.35, 1, 0.14, 1, 0.04, 0.13, 30, 1.11879, 0.029903, 0.08, 0.09065261, 0.1365994, 0, 0, 0.2, 4, 75.1592, 1.6, -0.042194377, 0.01, 0.056546969, 0.0448, 1, 1, 0.1884146, 0.2742203, 1, 0.0535, 0.8, 0.530451, 1, 1, 0.01, 0.282092928, 0.314469636, 0.915406, 1, 4, 0.8507, 0.155, 0.5, 1, 1.2339, 1, 0.003, 0.700904682321678, 6.4, 0.185277, 0.2, 30, 1.07687, 0.37229, 0.08, 0.1585843, 2, 0.03, 0.5, -0.003146882, 0.01935873, 0.74, 0.01585536, 1, -6, 0.013, 0.97, 0.87, 12, 0.126704476891517, 0.056147521, 0, 0, 1, 0.0000032, 0.03468189, 0.1897134, 0.1246998, 0.09166008, 0.064085801, 0.1111355, 0, 0.024434906, 0.024434906, 0.0172865778595673, 0.03, 0.102013522823697, 1, 1, 1, 0.2721489, 0.08703155, 0.2, 4, 23.17884, 1.5, -2.058459869, 0.061548045, 0.035, 1, 0.0225, 1, 0.45, 0.34, 0.929015, 0.112093367029781, 0.965, 0.024740401610319, 1, 0.0265, 1, 0.145, 1.5, 3, 0.6, 0.006, 0.00055, 4, 1, 0.887389870407265, 0.077770133, 0.0002356039, 0.2, 1.3, 0.3665807, 0.68, 0.7762527, 0.4840946, 2, 0.016, 4, 0.02, 0.03, 0.03, 0.03, 0.03, 0.03, -0.0003904036, 0.007269213, 0.003295476, 0.01509832, 0.00492403, 0, 0, 0.5, 0, 0.5, 0, 0, 0, 1560.2222, 0, 15, 0, 0.064085801, 0.024434906, 1.77651522362, 0, 0, 0, 0, 1, 0.58133, 0.00044, 0.241, 0, 1, 0}
#define SamplesExogVarForPython			{1.81, 1.81, 1.81, 1.328, 1.328, 1.328, 1.328, 1.328, 4.964, 4.964, 4.964, 4.964, 4.964, 10.227, 10.227, 10.227, 10.227, 10.227, 3.573, 3.573, 3.573, 3.573, 3.573, 3.495, 3.495, 3.495, 3.495, 3.495, 1.255, 1.255, 1.255, 1.255, 1.255, 1.663, 1.663, 1.663, 1.43, 1.43, 1.43, 1.43, 1.43, 5.779, 5.779, 5.779, 5.779, 5.779, 23.867, 23.867, 23.867, 23.867, 23.867, 14.767, 14.767, 14.767, 14.767, 14.767, 8.863, 8.863, 8.863, 8.863, 8.863, 2.964, 2.964, 2.964, 2.964, 2.964, 0.093, 0.093, 0.093, 0.365, 0.365, 0.365, 0.365, 0.365, 0.508, 0.508, 0.508, 0.508, 0.508, 0.398, 0.398, 0.398, 0.398, 0.398, 0.729, 0.729, 0.729, 0.729, 0.729, 0.876, 0.876, 0.876, 0.876, 0.876, 0.655, 0.655, 0.655, 0.655, 0.655, 0.071, 0.071, 0.071, 0.262, 0.262, 0.262, 0.262, 0.262, 0.375, 0.375, 0.375, 0.375, 0.375, 0.079, 0.079, 0.079, 0.079, 0.079, 0.387, 0.387, 0.387, 0.387, 0.387, 0.162, 0.162, 0.162, 0.162, 0.162, 0.117, 0.117, 0.117, 0.117, 0.117, 1.869, 1.869, 1.869, 8.624, 8.624, 8.624, 8.624, 8.624, 10.95, 10.95, 10.95, 10.95, 10.95, 13.816, 13.816, 13.816, 13.816, 13.816, 16.935, 16.935, 16.935, 16.935, 16.935, 19.097, 19.097, 19.097, 19.097, 19.097, 18.496, 18.496, 18.496, 18.496, 18.496, 1.324, 1.324, 1.324, 6.116, 6.116, 6.116, 6.116, 6.116, 7.737, 7.737, 7.737, 7.737, 7.737, 9.672, 9.672, 9.672, 9.672, 9.672, 27.158, 27.158, 27.158, 27.158, 27.158, 13.136, 13.136, 13.136, 13.136, 13.136, 12.822, 12.822, 12.822, 12.822, 12.822, 1.807, 1.807, 1.807, 13.471, 13.471, 13.471, 13.471, 13.471, 8.276, 8.276, 8.276, 8.276, 8.276, 3.385, 3.385, 3.385, 3.385, 3.385, 9.385, 9.385, 9.385, 9.385, 9.385, 31.541, 31.541, 31.541, 31.541, 31.541, 12.654, 12.654, 12.654, 12.654, 12.654, 1.341, 1.341, 1.341, 11.14, 11.14, 11.14, 11.14, 11.14, 5.236, 5.236, 5.236, 5.236, 5.236, 17.371, 17.371, 17.371, 17.371, 17.371, 10.057, 10.057, 10.057, 10.057, 10.057, 23.927, 23.927, 23.927, 23.927, 23.927, 10.867, 10.867, 10.867, 10.867, 10.867, 6.839, 6.839, 6.839, 5.591, 5.591, 5.591, 5.591, 5.591, 1.66, 1.66, 1.66, 1.66, 1.66, 1.432, 1.432, 1.432, 1.432, 1.432, 2.276, 2.276, 2.276, 2.276, 2.276, 9.7, 9.7, 9.7, 9.7, 9.7, 9.024, 9.024, 9.024, 9.024, 9.024, 0.292, 0.292, 0.292, 0.036, 0.036, 0.036, 0.036, 0.036, 0.058, 0.058, 0.058, 0.058, 0.058, 0.245, 0.245, 0.245, 0.245, 0.245, 0.102, 0.102, 0.102, 0.102, 0.102, 0.208, 0.208, 0.208, 0.208, 0.208, 0.388, 0.388, 0.388, 0.388, 0.388, 2.721, 2.721, 2.721, 1.154, 1.154, 1.154, 1.154, 1.154, 1.154, 1.154, 1.154, 1.154, 1.154, 1.421, 1.421, 1.421, 1.421, 1.421, 1.344, 1.344, 1.344, 1.344, 1.344, 0.994, 0.994, 0.994, 0.994, 0.994, 1.315, 1.315, 1.315, 1.315, 1.315, 2.489, 2.489, 2.489, 0.737, 0.737, 0.737, 0.737, 0.737, 2.275, 2.275, 2.275, 2.275, 2.275, 1.123, 1.123, 1.123, 1.123, 1.123, 2.46, 2.46, 2.46, 2.46, 2.46, 0.952, 0.952, 0.952, 0.952, 0.952, 2.395, 2.395, 2.395, 2.395, 2.395, 0.41, 0.41, 0.41, 0.422, 0.422, 0.422, 0.422, 0.422, 0.464, 0.464, 0.464, 0.464, 0.464, 0.52, 0.52, 0.52, 0.52, 0.52, 0.535, 0.535, 0.535, 0.535, 0.535, 0.654, 0.654, 0.654, 0.654, 0.654, 0.444, 0.444, 0.444, 0.444, 0.444, 0.54, 0.54, 0.54, 0.565, 0.565, 0.565, 0.565, 0.565, 0.604, 0.604, 0.604, 0.604, 0.604, 0.896, 0.896, 0.896, 0.896, 0.896, 0.588, 0.588, 0.588, 0.588, 0.588, 0.91, 0.91, 0.91, 0.91, 0.91, 0.9, 0.9, 0.9, 0.9, 0.9, 0.782, 0.782, 0.782, 0.769, 0.769, 0.769, 0.769, 0.769, 0.761, 0.761, 0.761, 0.761, 0.761, 0.786, 0.786, 0.786, 0.786, 0.786, 0.913, 0.913, 0.913, 0.913, 0.913, 0.764, 0.764, 0.764, 0.764, 0.764, 0.815, 0.815, 0.815, 0.815, 0.815, 0.729, 0.729, 0.729, 0.874, 0.874, 0.874, 0.874, 0.874, 0.706, 0.706, 0.706, 0.706, 0.706, 0.93, 0.93, 0.93, 0.93, 0.93, 0.754, 0.754, 0.754, 0.754, 0.754, 0.992, 0.992, 0.992, 0.992, 0.992, 0.991, 0.991, 0.991, 0.991, 0.991, 12.467, 12.467, 12.467, 12.333, 12.333, 12.333, 12.333, 12.333, 12.296, 12.296, 12.296, 12.296, 12.296, 15.382, 15.382, 15.382, 15.382, 15.382, 18.31, 18.31, 18.31, 18.31, 18.31, 19.794, 19.794, 19.794, 19.794, 19.794, 20.78, 20.78, 20.78, 20.78, 20.78, 0.003, 0.003, 0.003, 0.002, 0.002, 0.002, 0.002, 0.002, 0.012, 0.012, 0.012, 0.012, 0.012, 0.01, 0.01, 0.01, 0.01, 0.01, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.112, 0.112, 0.112, 0.127, 0.127, 0.127, 0.127, 0.127, 0.164, 0.164, 0.164, 0.164, 0.164, 0.269, 0.269, 0.269, 0.269, 0.269, 0.395, 0.395, 0.395, 0.395, 0.395, 0.432, 0.432, 0.432, 0.432, 0.432, 0.421, 0.421, 0.421, 0.421, 0.421, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8.087, 8.087, 8.087, 8.355, 8.355, 8.355, 8.355, 8.355, 9.098, 9.098, 9.098, 9.098, 9.098, 9.977, 9.977, 9.977, 9.977, 9.977, 11.891, 11.891, 11.891, 11.891, 11.891, 12.856, 12.856, 12.856, 12.856, 12.856, 12.268, 12.268, 12.268, 12.268, 12.268, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7.353, 7.353, 7.353, 7.48, 7.48, 7.48, 7.48, 7.48, 8.623, 8.623, 8.623, 8.623, 8.623, 9.712, 9.712, 9.712, 9.712, 9.712, 9.72, 9.72, 9.72, 9.72, 9.72, 8.999, 8.999, 8.999, 8.999, 8.999, 7.383, 7.383, 7.383, 7.383, 7.383, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0.704, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.188, 0.188, 0.188, 0.188, 0.188, 0.85, 0.85, 0.85, 0.85, 0.85, 1.239, 1.239, 1.239, 1.239, 1.239, 1.197, 1.197, 1.197, 1.197, 1.197, 0, 0, 0, 0.086, 0.086, 0.086, 0.086, 0.086, 0.247, 0.247, 0.247, 0.247, 0.247, 0.297, 0.297, 0.297, 0.297, 0.297, 0.31, 0.31, 0.31, 0.31, 0.31, 0.179, 0.179, 0.179, 0.179, 0.179, 0.006, 0.006, 0.006, 0.006, 0.006, 0, 0, 0, 0, 0, 0, 0, 0, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.048, 0.048, 0.048, 0.048, 0.048, 0.131, 0.131, 0.131, 0.131, 0.131, 0.155, 0.155, 0.155, 0.155, 0.155, 0.136, 0.136, 0.136, 0.136, 0.136, 0.121, 0.121, 0.121, 0.121, 0.121, 0.065, 0.065, 0.065, 0.065, 0.065, 0, 0, 0, 0.02, 0.02, 0.02, 0.02, 0.02, 0.062, 0.062, 0.062, 0.062, 0.062, 0.045, 0.045, 0.045, 0.045, 0.045, 0.003, 0.003, 0.003, 0.003, 0.003, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.025, 0.025, 0.025, 0.085, 0.085, 0.085, 0.085, 0.085, 0.085, 0.085, 0.085, 0.085, 0.085, 0.085, 0.085, 0.085, 0.085, 0.085, 0.085, 0.085, 0.085, 0.085, 0.085, 0.085, 0.085, 0.085, 0.085, 0.085, 0.055, 0.055, 0.055, 0.055, 0.055, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.023, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.009, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 0.049, 31.132, 30.802, 30.9994420043439, 30.8294088358922, 30.6585902307201, 30.4968055154227, 30.2943501354624, 30.2378672233831, 30.0612243998512, 29.971707613587, 29.9120849431746, 29.9614081214607, 29.7427700292074, 29.4999419499806, 29.2960977762245, 29.0959735261256, 28.8797817944821, 28.6521725923119, 28.4618258087071, 28.288093001334, 28.1187292335614, 27.8822956842376, 27.5111404700889, 27.1197531074635, 26.821087440321, 26.629823515698, 26.5191642814984, 26.4685182805863, 26.366963006624, 26.181999950832, 25.9663611922083, 25.7586107849201, 25.5525225370469, 4.826, 4.774, 4.78772178091811, 4.76146093712741, 4.73507878623406, 4.71009187823937, 4.67882357243683, 4.67010004546581, 4.64281837073283, 4.62899291325217, 4.61978446499268, 4.62740220388461, 4.59363455231614, 4.55613086809596, 4.524648069455, 4.49373979597852, 4.46034997359724, 4.42519677520693, 4.39579858663098, 4.3689663505603, 4.34280889263736, 4.30629281426154, 4.24896959203605, 4.18852160718022, 4.14239406334926, 4.11285422654533, 4.09576341485384, 4.08794137206839, 4.07225662532204, 4.04368992883904, 4.01038551060699, 3.97829941209499, 3.94647002648878, 9.651, 9.549, 9.57558203517544, 9.52305958806229, 9.47029452323531, 9.42031998455972, 9.35778246859408, 9.34033516234499, 9.2857710238222, 9.25811970899278, 9.23970254614158, 9.25493824425021, 9.18740196446516, 9.11239351132092, 9.04942700347475, 8.9876095625743, 8.92082895209143, 8.85052153858907, 8.79172431116528, 8.738059062966, 8.68574339057856, 8.61271017768716, 8.49806207529983, 8.37716435727557, 8.28490793548537, 8.22582740750877, 8.19164528981516, 8.17600097801048, 8.14463103087421, 8.0874968116852, 8.02088701197089, 7.95671388693365, 7.89305419513278, 17.619, 17.432, 17.5703341304178, 17.4739601510883, 17.3771409900162, 17.2854421941291, 17.1706914617803, 17.13867721979, 17.0385569198581, 16.9878192373952, 16.9540253955336, 16.9819815349615, 16.8580585193798, 16.720424735918, 16.6048868419478, 16.4914573827548, 16.3689209525611, 16.2399131551715, 16.132025516803, 16.0335545999868, 15.9375600337319, 15.8035506389603, 15.593181654708, 15.3713451863359, 15.2020629275054, 15.0936554580339, 15.0309343381108, 15.0022284292022, 14.9446673900076, 14.8398312225826, 14.7176082148279, 14.5998562865425, 14.4830464621922, 0.185, 0.183, 0.184386831136353, 0.183375462057048, 0.182359421145654, 0.181397114437816, 0.180192895795682, 0.179856931517029, 0.178806247750868, 0.178273795697361, 0.177919155918371, 0.17821253360383, 0.176912059066558, 0.175467700808971, 0.174255221525015, 0.173064868604981, 0.171778945190294, 0.170425109869008, 0.169292913997838, 0.168259539209625, 0.167252151771989, 0.165845828621785, 0.163638171665023, 0.161310172485838, 0.159533688382482, 0.158396037292924, 0.157737828492675, 0.157436582566487, 0.156832524753174, 0.155732351668445, 0.154449717375633, 0.153214003543694, 0.151988176351242, 57.339, 56.731, 57.4784825495366, 57.1632107938603, 56.8464826987178, 56.5465050431941, 56.1711167370924, 56.0663873656463, 55.7388601331092, 55.5728800797761, 55.4623290375871, 55.553782988339, 55.1483890535552, 54.6981425777503, 54.320179200783, 53.9491132243232, 53.5482552774969, 53.1262273083089, 52.7732904948573, 52.4511589501838, 52.1371283825021, 51.6987385031931, 51.0105506804372, 50.2848488536229, 49.7310695522216, 49.3764321960958, 49.1712502814988, 49.077343582171, 48.8890420301162, 48.5460876061894, 48.1462549697562, 47.761048740615, 47.3789244508492, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 14.8700141184589, 16267.053, 16605.123, 16806.6393482682, 17135.4724527525, 17528.8377562617, 17984.4398499099, 18456.4243946899, 19102.6383891572, 19871.6086384415, 20707.7664780121, 21563.3386591321, 22624.9459450606, 23645.7432804703, 24643.4289611723, 25646.6872547695, 26632.3071977868, 27565.4240820874, 28441.0707332984, 29315.4575801605, 30213.6179449334, 31165.5137269486, 32103.293594901, 32793.7284521049, 33197.9346251386, 33462.797561894, 33739.4323163035, 34120.402062431, 34708.7799881103, 35371.6308123105, 35953.0193605565, 36408.1126965599, 36769.8212914557, 37135.1234015857, 3768.44, 3846.758, 3895.5072632511, 3971.72546014171, 4062.90117737925, 4168.50237629722, 4277.90076250832, 4427.68271813297, 4605.91758884314, 4799.72545666098, 4998.03325494976, 5244.09665926031, 5480.70097687514, 5711.9483866089, 5944.48743791112, 6172.93820473409, 6389.21961144081, 6592.18034732319, 6794.8490809266, 7003.02813160026, 7223.66218317107, 7441.02439409489, 7601.05603071812, 7694.74448623111, 7756.13543254206, 7820.25489585289, 7908.55752330655, 8044.93401330703, 8198.57211707163, 8333.32858239062, 8438.81185951232, 8522.65006353387, 8607.32118628504, 2362.346, 2411.441, 2441.75636492054, 2489.53095621346, 2546.68112250661, 2612.87337480547, 2681.44575518914, 2775.33110022416, 2887.05111525607, 3008.53249440281, 3132.8344905133, 3287.07034300863, 3435.37711269529, 3580.32610044729, 3726.08470651285, 3869.28072086079, 4004.84881655453, 4132.06733655189, 4259.10282559202, 4389.59225551065, 4527.88864756811, 4664.13420588687, 4764.44418887669, 4823.16937332866, 4861.65004446419, 4901.84098676624, 4957.1902617267, 5042.67288054392, 5138.97531111581, 5223.44247666596, 5289.56081399634, 5342.11172828273, 5395.1847272354, 5007.457, 5114.715, 5189.68057623748, 5294.52253188587, 5419.40945156832, 5563.46164071173, 5712.57286629309, 5915.62542268501, 6156.82111441823, 6418.84391535105, 6686.99753457046, 7019.12340686456, 7338.87820253109, 7651.62724995882, 7966.40004723714, 8275.82296253122, 8569.21171508528, 8844.96711075933, 9120.42156662663, 9403.50142706598, 9703.53155236169, 9999.35758348466, 10218.3237227396, 10348.2225577011, 10434.7206255677, 10524.9935183415, 10647.8440912671, 10835.475495236, 11046.5485065449, 11232.2940758892, 11378.6663803837, 11495.9307904285, 11614.4036849656, 1160.447, 1185.303, 1201.07364360381, 1225.33773998187, 1254.24094229999, 1287.57965845832, 1322.08921263615, 1369.08267787279, 1424.90379904507, 1485.54504191166, 1547.60517061324, 1624.47071671214, 1698.47316288377, 1770.85423382051, 1843.70367127251, 1915.31495887053, 1983.21538026369, 2047.03482598105, 2110.78462369891, 2176.29920680554, 2245.73667419607, 2314.201167117, 2364.87759215652, 2394.94072700946, 2414.95940600349, 2435.8517115413, 2464.28363197935, 2507.70810304436, 2556.55778214022, 2599.54580509816, 2633.42147711673, 2660.56056403521, 2687.9793365434, 727.372, 742.952, 752.76162260153, 767.968917056603, 786.08372757737, 806.978454727901, 828.606993607673, 858.059706463035, 893.045069744339, 931.05139901476, 969.947001652486, 1018.12176055399, 1064.50209847356, 1109.86625469673, 1155.52395523326, 1200.40565698064, 1242.96160819599, 1282.95984624539, 1322.91443306542, 1363.97508254852, 1407.49436290289, 1450.40384064908, 1482.16481396121, 1501.00660130114, 1513.55312029449, 1526.64717651683, 1544.46661554674, 1571.68249483407, 1602.29857228743, 1629.24091182388, 1650.47217101537, 1667.48133878244, 1684.66579686534, 30.9481608938321, 28.423884732396, 26.1055002929609, 23.9762140876207, 22.2696387795287, 20.8297203297322, 19.5821177987474, 18.6454663908314, 17.9293017417464, 17.3344317770234, 16.77183248516, 16.3474691515797, 15.8646506499198, 15.3686052409316, 14.8854676259798, 14.3958892047468, 13.8774714916189, 13.3371332368263, 12.8102512778273, 12.3100478405237, 11.844377028786, 11.3776599580232, 10.8321013262191, 10.2193533808506, 9.60706042033863, 9.04405577024266, 8.54880236128878, 8.13412115707488, 7.75465309646599, 7.37395793272008, 6.98631240577975, 6.60309133358083, 6.24089113500557, 2.97317171521139, 2.73066598085417, 2.50794014380165, 2.30338086349337, 2.1394311718363, 2.00109904858567, 1.88124260316795, 1.79125905026534, 1.72245753131892, 1.6653087217528, 1.61126013685289, 1.57049179960979, 1.52410770856022, 1.47645291626017, 1.43003816818331, 1.3830046556143, 1.33320056914131, 1.28129058905212, 1.2306733474291, 1.18261909578086, 1.13788237327228, 1.09304513727114, 1.04063363861589, 0.981767301906145, 0.922944675325452, 0.86885714789724, 0.821278442577237, 0.781440261839192, 0.744984987210795, 0.708411825501768, 0.671170946465983, 0.634355122209302, 0.599558760986347, 35.6784246920866, 32.768326181329, 30.0955888605735, 27.6408524455167, 25.6734360675286, 24.013433647674, 22.5751416244388, 21.4953279697694, 20.6697013166326, 19.9839086031087, 19.3353189652485, 18.8460939256358, 18.289479152612, 17.7176158089661, 17.1606331478605, 16.596225237072, 15.9985701001375, 15.3756439819101, 14.7682308835921, 14.191573978848, 13.6547278300612, 13.1166755070542, 12.4877311046158, 11.7813278550314, 11.0754491323486, 10.4263921793797, 9.85544188881226, 9.3773788411719, 8.93991108113499, 8.50102866169349, 8.05413355255888, 7.61233915282785, 7.19477855681512, 6.68590280318198, 6.14056942710034, 5.63971598137711, 5.17971447570129, 4.81103354905897, 4.499959982107, 4.23043348947361, 4.02808349215801, 3.87336647193561, 3.74485341494608, 3.62331197035292, 3.53163440633594, 3.42732844822908, 3.32016500798988, 3.21579011006912, 3.11002376905363, 2.99802711589833, 2.88129484657941, 2.76746961545495, 2.65940789330279, 2.55880644573252, 2.45797896902363, 2.34011891271231, 2.20774357643181, 2.07546653305276, 1.95383751667294, 1.84684517659273, 1.75725929666946, 1.6752807074135, 1.59303702026265, 1.50929180761165, 1.42650243445171, 1.3482543171799, 909.961994036598, 835.741255129388, 767.574305413411, 704.967369643212, 654.789309769077, 612.451703075039, 575.768719205509, 548.228563078356, 527.171330812584, 509.680499575511, 493.13851586204, 480.661053742549, 466.464847123504, 451.879732646298, 437.674143209052, 423.279176155895, 408.036253721828, 392.14880640397, 376.657011603065, 361.94963953032, 348.25762268101, 334.534842906822, 318.493901987478, 300.477408402537, 282.474292637651, 265.920390264883, 251.358562791157, 239.165782200075, 228.008365955232, 216.814869465709, 205.41701297, 194.149247747658, 183.499554666811}
#define NSamplesVarExogVarForPython		{33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33}
#define NVarExogVarForPython			{52}


typedef long long unsigned int TInt;
#endif