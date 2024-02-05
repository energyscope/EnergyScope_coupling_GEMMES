#include <iostream>
#include <fstream>
#include<math.h>
#include <Rcpp.h>
using namespace Rcpp; 

#define dim 69
#define dimIv 227
#define dimOut 365

//Note: All pieces of code beginning with a @ will be replaced by the required code by R before compiling
//For instance @AddDim will be replaced by the dimension of the model

// utility function that converts a Rcpp::List to a double**
// WARNING: do not forget to free the double** after use!
template<typename T>
void RcppListToPptr(Rcpp::List L, T**& pptr) {
	for (unsigned int it=0; it<L.size(); it++) {
		std::vector<double> tempVec = L[it];
		pptr[it] = (double*) malloc(sizeof(*pptr[it]) * tempVec.size());
		for (unsigned int it2=0; it2<tempVec.size(); it2++) {
			pptr[it][it2] = tempVec[it2];
		}
	}
}

void Func(double t, double* y, double* parms, double* ydot, double* x, double** dataExogVar, double** exogSamplingTime, int nExogVar, int* comptExogVar) {

x[3] = parms[2] * y[0];
x[14] = parms[8] * pow((y[11]/(y[61] * y[57] * (1.0 + parms[24]))), parms[9]) + parms[10] * pow((y[60]/y[59]), parms[11]);
x[15] = parms[12] * pow((y[11]/(y[61] * y[57] * (1.0 + parms[24]))), parms[13]) + parms[14] * pow((y[60]/y[59]), parms[15]);
x[16] = parms[16] * pow((y[11]/(y[61] * y[57] * (1.0 + parms[24]))), parms[17]) + parms[18] * pow((y[60]/y[59]), parms[19]);
x[18] = y[61] * y[57];
x[19] = y[61] * y[57]/y[11];
x[20] = y[9] * y[63] * y[57] + y[8] * y[64] * y[62] * y[57];
x[22] = parms[20] * pow((y[62] * y[57]/y[11]), parms[21]) + parms[22] * (pow((y[59]/y[60]), parms[23]));
x[24] = parms[25] - parms[26] * (y[1]/y[0] - parms[2]);
x[26] = (y[11] * (1.0 - y[5]) + y[61] * y[57] * (1.0 + parms[24]) * y[5]) * (1.0 + parms[27] + parms[28]);
x[27] = (y[11] * (1.0 - y[6]) + y[61] * y[57] * (1.0 + parms[24]) * y[6]) * (1.0 + parms[29]);
x[28] = (y[11] * (1.0 - y[7]) + y[61] * y[57] * (1.0 + parms[24]) * y[7]) * (1.0 + parms[30]);
x[49] = parms[45] * y[37];
x[50] = parms[46] * y[17];
x[55] = parms[49] * y[18];
x[61] = parms[56] * (y[17] + y[37] + y[15] * y[57]);
x[65] = 0.0;
x[67] = 0.155;
x[80] = parms[70] + parms[71]/(1.0 + exp(-parms[72] * ((y[15] * y[57] + y[16] * y[57])/(y[17] + y[15] * y[57] + y[16] * y[57]))));
x[81] = y[45] + y[36] + y[13];
x[83] = y[23] - y[22] - y[15];
x[85] = y[67] + parms[82];
x[86] = y[67] + parms[83];
x[89] = y[33];
x[92] = 0.0;
x[111] = parms[99] * (y[9] * y[63] * y[57]);
x[120] = parms[103] * y[65];
x[122] = parms[105] * y[44];
x[129] = y[32] + y[53];
x[136] = parms[120] * y[64] * y[61];
x[141] = 0.025076004145812;
x[148] = parms[168];
x[149] = y[67] + parms[124];
x[164] = parms[132] * y[9];
x[169] = parms[138] * y[18];
x[175] = parms[179] * (parms[181] * y[23] - y[22]);
x[181] = parms[174] * (parms[175] * (y[15] + y[16]) - y[14]);
x[198] = parms[184] * y[35];
x[200] = 0.0;
x[207] = parms[180] * (parms[187] * (y[51] + y[49]) - y[47]);
x[217] = parms[163] * (y[57] - y[58]);
x[218] = parms[164] * y[59];
x[219] = parms[165] * y[60];
x[220] = parms[168] * y[61];
x[221] = parms[168] * y[62];
x[222] = parms[170] * y[63];
x[223] = parms[166] * y[64];
x[224] = parms[167] * y[65];
ydot[9] = x[164];
ydot[14] = x[181];
ydot[18] = x[169];
ydot[22] = x[175];
ydot[39] = x[198];
ydot[40] = x[200];
ydot[47] = x[207];
ydot[58] = x[217];
ydot[59] = x[218];
ydot[60] = x[219];
ydot[61] = x[220];
ydot[62] = x[221];
ydot[63] = x[222];
ydot[64] = x[223];
ydot[65] = x[224];
x[2] = parms[0] * (x[3] - y[1]);
x[8] = x[89] + y[43];
x[21] = x[20]/(y[9] + y[8] * y[64]);
x[23] = (1.0 + x[24]) * y[10];
x[48] = x[49] + x[50];
x[52] = parms[47] * y[34] * x[28];
x[53] = parms[48] * y[3] * x[28];
x[62] = parms[57] * (x[61] - y[27]);
x[68] = parms[58] - parms[59]/(1.0 + exp(-parms[60] * (y[24]/x[81])));
x[87] = y[32] * y[24] + x[85] * y[56] * y[57] - x[67] * y[46];
x[121] = parms[104] * x[120];
x[123] = x[122] * x[28];
x[160] = parms[128] * (x[14] - y[5]);
x[161] = parms[129] * (x[15] - y[6]);
x[162] = parms[130] * (x[16] - y[7]);
x[163] = parms[131] * (x[22] - y[8]);
x[190] = parms[146] * (x[80] - y[31]);
x[193] = y[35]/x[28] - parms[151] * y[34];
x[204] = y[42]/x[28] - parms[101] * y[44];
x[215] = x[181] + x[175] + x[207];
x[225] = parms[191] * (x[148] - y[67]);
ydot[5] = x[160];
ydot[6] = x[161];
ydot[7] = x[162];
ydot[8] = x[163];
ydot[31] = x[190];
ydot[34] = x[193];
ydot[44] = x[204];
ydot[55] = x[215];
ydot[67] = x[225];
x[1] = y[0] + x[2];
x[51] = x[52] + x[53];
x[66] = (1.0 - x[68]) * y[32];
x[108] = parms[27] * x[8] * ((1.0 - y[5]) * y[11] + y[5] * y[61] * y[57] * (1.0 + parms[24]))/x[26];
x[115] = (1.0 + parms[100]) * y[41] * x[120] + x[27] * x[121] + parms[101] * x[28] * y[44];
x[166] = parms[133] * (x[23] - y[11]);
x[186] = x[62];
x[202] = parms[156] * (x[123] - y[42]);
ydot[11] = x[166];
ydot[27] = x[186];
ydot[42] = x[202];
x[10] = parms[4] * x[1];
x[54] = x[51] + x[48];
x[70] = ((x[66] * y[45] + x[66] * (1.0 - parms[36]) * y[13] + x[66] * (1.0 - parms[54]) * y[36]) + y[32] * y[24])/(x[81] + y[24]);
x[84] = parms[79] + parms[80] * (x[166]/y[11] - parms[81]);
x[91] = (1.0/(1.0 + exp(-parms[84] * (x[66] - parms[85] - x[166]/y[11])))) * (parms[97] - parms[98]) + parms[98];
x[116] = x[115] + y[43];
x[140] = x[141] * x[1] * y[11];
x[171] = (parms[147] * (x[218]/y[59]) + parms[148] * x[166]/y[11]) * y[20];
x[201] = (parms[154] * (x[218]/y[59]) + parms[155] * x[166]/y[11]) * y[41];
ydot[20] = x[171];
ydot[41] = x[201];
x[9] = x[27] * (x[10] + x[121] + x[55]);
x[56] = parms[50] * x[54];
x[58] = x[54] - x[27] * x[55] - parms[52] * x[54] - (1.0 + parms[53]) * y[20] * y[18];
x[69] = x[70] * (1.0 + y[28]);
x[142] = parms[121] * x[140];
x[144] = (1.0 - parms[121]) * x[140];
x[191] = parms[149] * (x[84] - y[32]);
ydot[32] = x[191];
x[72] = x[69] * (1.0 + y[29]);
x[143] = parms[122] * x[142];
x[170] = x[56]/x[28] - parms[139] * y[19];
ydot[19] = x[170];
x[0] = (y[4] + x[143]/x[28])/y[3] - parms[1];
x[11] = x[28] * y[4] + y[35] + x[56] + y[42] + x[143];
x[145] = x[142] - x[143];
x[158] = y[4] + x[143]/x[28] - parms[1] * y[3];
ydot[3] = x[158];
x[6] = x[8] + x[9] + x[11] + x[20];
x[7] = x[8]/x[26] + x[9]/x[27] + x[11]/x[28] + x[20]/x[21];
x[13] = y[5] * (x[8]/x[26]) + y[6] * (x[9]/x[27]) + y[7] * (x[11]/x[28]);
x[109] = parms[28] * x[8] * ((1.0 - y[5]) * y[11] + y[5] * y[61] * y[57] * (1.0 + parms[24]))/x[26] + parms[29] * x[9] * ((1.0 - y[6]) * y[11] + y[6] * y[61] * y[57] * (1.0 + parms[24]))/x[27] + parms[30] * x[11] * ((1.0 - y[7]) * y[11] + y[7] * y[61] * y[57] * (1.0 + parms[24]))/x[28];
x[4] = x[1] - x[13];
x[17] = x[13] * y[61] * y[57];
x[139] = x[20] - x[13] * y[61] * y[57];
x[155] = parms[126] * (x[7] - y[0]) + x[0] * y[0];
x[156] = x[1] - x[7];
x[172] = std::max(parms[192] * x[13] * y[61] - y[56], 0.0);
ydot[0] = x[155];
ydot[1] = x[156];
ydot[56] = x[172];
x[5] = x[4]/(y[3] * parms[3]);
x[30] = x[4]/y[59];
x[46] = x[89] + y[43] + x[115] + x[11] + x[20] - x[17];
x[71] = parms[61] + parms[62]/(1.0 + exp(-parms[63] * ((y[17] + y[15] * y[57] + y[16] * y[57])/y[11] * x[4])));
x[77] = parms[77] * pow((x[17]/(y[54] * y[57])), 2.0);
x[103] = parms[94] - parms[95] * x[72] + parms[96] * (x[155]/y[0]);
x[107] = 0.064085801 * x[17];
x[110] = parms[33] * y[11] * x[4] + parms[52] * x[54];
x[150] = -0.0003904036 * x[4] * y[11];
x[151] = 0.007269213 * x[4] * y[11];
x[152] = 0.003295476 * x[4] * y[11];
x[153] = 0.01509832 * x[4] * y[11];
x[154] = 0.00492403 * x[4] * y[11];
x[209] = -parms[190] * (y[68] * x[139]/y[57]);
x[210] = -parms[189] * x[139];
x[211] = -(1.0 - parms[190]) * (y[68] * x[139]/y[57]);
ydot[49] = x[209];
ydot[50] = x[210];
ydot[51] = x[211];
x[25] = ((1.0 + parms[34]) * y[12] * x[30] + x[27] * x[10] + parms[33] * y[11] * x[4])/x[4];
x[29] = x[30] + x[120] + y[18];
x[32] = x[6] - x[17] - x[107] - parms[33] * y[11] * x[4] - x[109] - x[108] - x[27] * x[10] - x[53] - x[50] - (1.0 + parms[34]) * y[12] * x[30];
x[75] = parms[75] + parms[76] * pow((x[77]), parms[74]);
x[76] = ((y[16] + y[23] + y[49] + y[51] - y[55]) * y[57])/x[46];
x[78] = parms[67] + parms[68]/(1.0 + exp(-parms[69] * (x[77])));
x[94] = y[12] * x[30] + y[41] * x[120] + y[20] * y[18];
x[95] = parms[34] * y[12] * x[30] + parms[100] * y[41] * x[120] + parms[53] * y[20] * y[18];
x[117] = parms[102] * x[46];
x[124] = parms[106] * y[12] * (y[65] - x[120] - x[30] - y[18]);
x[130] = parms[108] + parms[110]/(1.0 + exp(-parms[111] * ((y[48] + y[49] * y[57] + y[51] * y[57])/x[46])));
x[131] = parms[109] + parms[110]/(1.0 + exp(-parms[111] * ((y[48] + y[49] * y[57] + y[51] * y[57])/x[46])));
x[134] = -(y[54] * y[57] + y[55] * y[57] - y[23] * y[57] - y[16] * y[57] - y[49] * y[57] - y[51] * y[57] - y[50])/x[46];
x[135] = -(y[54] * y[57] + y[55] * y[57] - y[23] * y[57] - y[16] * y[57] - y[49] * y[57] - y[51] * y[57] - y[50])/x[46];
x[157] = parms[127] * (x[5] - y[2]);
x[168] = parms[172] * (parms[173] * y[12] * x[30] * (1.0 + parms[34]) - y[13]);
x[187] = parms[142] * (x[71] - y[28]);
ydot[2] = x[157];
ydot[13] = x[168];
ydot[28] = x[187];
x[31] = 1.0 - x[29]/y[65];
x[33] = parms[31] * x[32];
x[34] = parms[32] * x[32];
x[35] = parms[35] * (x[32]);
x[47] = y[67] + parms[44] * x[75];
x[57] = (1.0 - parms[51]) * x[124];
x[74] = y[67] + x[75];
x[96] = x[95] + parms[89] * x[94];
x[125] = parms[51] * x[124];
x[132] = y[67] + parms[115] * x[75];
x[165] = parms[171] * (x[25] - y[10]);
x[167] = (parms[134] * (x[218]/y[59]) + parms[135] * (x[29]/y[65] - parms[136]) + parms[137] * x[166]/y[11]) * y[12];
x[189] = parms[145] * (x[78] - y[30]);
x[197] = parms[183] * x[94];
x[203] = parms[157] * (x[117] - y[43]);
x[212] = parms[159] * (x[130] - y[52]);
x[213] = parms[160] * (x[131] - y[53]);
ydot[10] = x[165];
ydot[12] = x[167];
ydot[30] = x[189];
ydot[38] = x[197];
ydot[43] = x[203];
ydot[52] = x[212];
ydot[53] = x[213];
x[79] = x[74] * (1.0 + parms[78] * y[28]);
x[97] = parms[90] * x[96];
x[98] = (1.0 - parms[90]) * x[96];
x[100] = parms[91] - parms[92] * x[72] - parms[93] * x[31];
x[113] = x[116] + (1.0 + parms[100]) * y[41] * x[120] + x[27] * x[121] + y[42] + x[125];
x[133] = (1.0 - parms[112]) * x[132];
x[36] = x[32] - x[111] - x[69] * y[17] - x[79] * y[15] * y[57] - x[47] * y[16] * y[57] + x[66] * (1.0 - parms[36]) * y[13] - (x[35] + x[33] + x[34]);
x[59] = x[72] * y[37] + x[69] * y[17] + x[79] * y[15] * y[57] + x[129] * y[25] - (x[66] * y[45] + x[66] * (1.0 - parms[36]) * y[13] + x[66] * (1.0 - parms[54]) * y[36]) - x[74] * y[23] * y[57] + x[86] * y[21] * y[57] - y[32] * y[24] - x[27] * x[55] - parms[52] * x[54] - (1.0 + parms[53]) * y[20] * y[18] + x[98] - x[57] + x[51] + x[48];
x[114] = x[129] * y[48] + x[132] * y[49] * y[57] + x[133] * y[51] * y[57];
x[37] = (1.0 - parms[37]) * x[36];
x[60] = (1.0 - parms[55]) * x[59];
x[106] = parms[88] * x[94] + parms[37] * x[36] + parms[55] * x[59];
x[112] = x[113] + x[114];
x[38] = x[37]/(x[28] * y[3]);
x[39] = x[37] - x[181] * y[57] - x[168];
x[63] = x[60] - x[62] - x[151];
x[105] = x[106] + x[107] + x[108] + x[109] + x[110];
x[118] = 0.112093367029781 * x[112];
x[119] = 0.024740401610319 * x[112];
x[12] = (parms[5] + parms[6] * (x[38] - x[166]/y[11]) + parms[7] * x[5]) * y[3];
x[40] = (1.0 - parms[42]) * x[39];
x[41] = parms[42] * x[39] - x[150];
x[64] = x[63];
x[205] = parms[185] * (x[118] - y[45]);
x[206] = parms[186] * (x[119] - y[46]);
ydot[45] = x[205];
ydot[46] = x[206];
x[42] = (parms[38] + parms[39] * (y[9] * y[63])/(x[46]/y[57])) * x[40];
x[43] = (parms[40] + parms[41] * (y[9] * y[63])/(x[46]/y[57])) * x[40];
x[45] = x[28] * y[4] - x[41];
x[159] = parms[169] * (x[12] - y[4]);
ydot[4] = x[159];
x[44] = x[40] - x[42] - x[43];
x[104] = x[105] + x[111] + x[34] + x[97] + x[66] * y[45] + x[67] * y[46] + x[43] - x[152];
x[138] = (x[136] + x[85] * y[56] + x[86] * y[21] - x[132] * y[49] - x[133] * y[51] - x[74] * y[23] - x[47] * y[16]) * y[57] - x[42] - x[65] + x[154] - x[129] * y[50];
x[178] = parms[176] * (x[45]/y[57]);
x[180] = (1.0 - parms[178]) * parms[177] * (x[45]/y[57]);
ydot[16] = x[180];
x[93] = (1.0 - parms[88]) * x[94] + x[35] + x[95] + x[124] - x[96] - x[72] * y[37] + x[66] * (1.0 - parms[54]) * y[36] + x[44] + x[64] + x[136] * y[57] + x[33] - x[52] - x[49] + x[153];
x[126] = x[112] - x[104] - x[115] - x[87];
x[137] = -(x[139] + x[138])/x[46];
x[176] = (parms[182] * x[186]/y[57] + x[178]);
x[179] = (1.0 - parms[193]) * x[178];
ydot[15] = x[179];
x[73] = parms[64] + parms[65]/(1.0 + exp(-parms[66] * (y[37]/x[93])));
x[90] = y[40] * x[93];
x[99] = x[100] * x[93];
x[101] = x[93] - x[89];
x[127] = x[126] + x[205] + x[206] + x[207] * y[57];
x[128] = parms[113] + parms[114] * x[137];
x[174] = x[176] - x[175] - x[179];
x[177] = (1.0 - parms[193]) * x[176];
x[182] = x[45] - x[179] * y[57] - x[180] * y[57] - x[145];
ydot[17] = x[182];
ydot[23] = x[177];
x[102] = y[35] - x[101];
x[146] = x[13] * y[61] + x[132] * y[49] + x[133] * y[51] + x[74] * y[23] + x[47] * y[16] + x[42]/y[57] + x[65]/y[57] + x[174] + x[215] + x[129] * y[50]/y[57];
x[147] = x[20]/y[57] + x[136] + x[154]/y[57] + x[85] * y[56] + x[86] * y[21] + x[140]/y[57] + x[209] + x[211] + x[180] + x[177] + x[210]/y[57] - x[172];
x[188] = parms[144] * (x[73] - y[29]);
x[194] = parms[152] * (x[99] - y[35]);
x[199] = parms[153] * (x[90] - y[66]);
x[208] = x[127] - x[209] * y[57] - x[211] * y[57];
x[214] = (x[139]/y[57] + x[138]/y[57] + x[140]/y[57] + x[209] + x[210]/y[57] + x[211] + x[180] + x[177] - x[215]);
x[226] = parms[195] * (x[128] - y[68]);
ydot[29] = x[188];
ydot[35] = x[194];
ydot[48] = x[208];
ydot[54] = x[214];
ydot[66] = x[199];
ydot[68] = x[226];
x[88] = x[91] * x[93] + x[92] * (y[36] + y[38]) + x[199];
x[173] = x[214] - x[172];
x[184] = x[208] - x[210];
x[196] = x[199] + x[198];
x[216] = parms[162] * ((x[146] - x[147])/x[147]);
ydot[21] = x[173];
ydot[25] = x[184];
ydot[37] = x[196];
ydot[57] = x[216];
x[192] = parms[150] * (x[88] - y[33]);
x[195] = x[101] - y[35] + x[196] - x[197];
ydot[33] = x[192];
ydot[36] = x[195];
x[82] = (x[182] + x[196] + x[184]) + x[56] + parms[73] * (x[205] + x[195] + x[168]) - (x[205] + x[195] + x[168] + x[186] + x[144]) - x[197] + (x[175] * y[57] + x[179] * y[57] - x[177] * y[57] + x[173] * y[57]);
x[185] = parms[73] * ((x[205] + x[195] + x[168]));
ydot[26] = x[185];
x[183] = std::max(x[82], -y[24]);
ydot[24] = x[183];
}
	
Rcpp::NumericMatrix RK4(int nt, 
                      double byT,
                      std::vector<double> Ry0,
                      std::vector<double> Rparms, 
                      double** dataExogVar,
                      double** exogSamplingTime, 
                      int nExogVar) {
	int it, it1;
	double *y = &Ry0[0];
	double *parms = &Rparms[0];
	double y1[dim], y2[dim], y3[dim], ydot0[dim], ydot1[dim], ydot2[dim], ydot3[dim], ydots[dim], x0[dimIv], x1[dimIv], x2[dimIv], x3[dimIv];
	Rcpp::NumericMatrix out(nt, dimOut);

	for (it=0; it<dim;it++) { //init out vector
		out(0, it)=y[it];
	}
	int comptExogVar[nExogVar];
	for (it=0; it<nExogVar; it++) comptExogVar[it]=1;

	// get intermediateVar and compute distance at t=0 //
	Func(0, y, parms, ydot0, x0, dataExogVar, exogSamplingTime, nExogVar, comptExogVar); 
						for (it1=0; it1<dim; it1++) {
							out(0, dim+it1) = ydot0[it1];
						}
						for (it1=0; it1<dimIv; it1++) {
							out(0, 2*dim+it1) = x0[it1];
						}
						 
	
	for (it=0; it<nExogVar; it++) comptExogVar[it]=1;
	
	for (it=0; it<(nt-1); it++) {

			
			

			Func(it*byT, y, parms, ydot0, x0, dataExogVar, exogSamplingTime, nExogVar, comptExogVar);

			for (it1=0; it1<dim; it1++)
				y1[it1] = y[it1] + ydot0[it1]*0.5*byT;
			Func((it + 0.5)*byT, y1, parms, ydot1, x1, dataExogVar, exogSamplingTime, nExogVar, comptExogVar);
			for (it1=0; it1<dim; it1++)
				y2[it1] = y[it1] + ydot1[it1]*0.5*byT;
			Func((it + 0.5)*byT, y2, parms, ydot2, x2, dataExogVar, exogSamplingTime, nExogVar, comptExogVar);
			for (it1=0; it1<dim; it1++)
				y3[it1] = y[it1] + ydot2[it1]*byT;
			Func((it+1)*byT, y3, parms, ydot3, x3, dataExogVar, exogSamplingTime, nExogVar, comptExogVar);
			for (it1=0; it1<dim; it1++) {
				ydots[it1] = (ydot0[it1] + 2.0*ydot1[it1] + 2.0*ydot2[it1] + ydot3[it1])/6.0;

				y[it1] = y[it1] + byT*ydots[it1];
				out(it+1, it1) = y[it1];
			}
			
			for(it1=0;it1<dim;it1++){
							out(it+1, dim+it1) = ydots[it1];
						}
						for(it1=0;it1<dimIv;it1++){
							out(it+1, 2*dim+it1) = (x0[it1] + 2.0*x1[it1] + 2.0*x2[it1] + x3[it1])/6.0;
						}
				
	}
	return out;
}

// [[Rcpp::export]]
Rcpp::NumericMatrix RK4(int nt, 
                        double byT,
                        std::vector<double> Ry0,
                        std::vector<double> Rparms, 
                        Rcpp::List RdataExogVar,
                        Rcpp::List RexogSamplingTime) {
	double** dataExogVar = (double**) malloc(sizeof(double*)*RdataExogVar.size());
	RcppListToPptr(RdataExogVar, dataExogVar);
	double** exogSamplingTime = (double**) malloc(sizeof(double*)*RexogSamplingTime.size());
	RcppListToPptr(RexogSamplingTime, exogSamplingTime);
	int nExogVar = RdataExogVar.size();
	Rcpp::NumericMatrix out = RK4(nt, byT, Ry0, Rparms, dataExogVar, exogSamplingTime, nExogVar);
	for (unsigned int it=0; it<RdataExogVar.size(); it++) {
		free(dataExogVar[it]);
		free(exogSamplingTime[it]);
	}
	free(dataExogVar);
	free(exogSamplingTime);
	
	return out;
}
