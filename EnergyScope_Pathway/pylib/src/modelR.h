#ifndef modelR_h
#define modelR_h

#include <iostream>
#include <fstream>
#include <math.h>
#include <cstring>
#include <stdio.h>
#include <string.h>

#if UseRCPP==1
        #include "preprocRCPP_R.h"
#else
        #include "preproc.h"    
#endif

#include "ODE.h"
#include "exogenousVariables.h"

using namespace std;

// GOODWIN-KEEN BUT WITH TWO EXOGENOUS VARIABLES (THIS IS JUST TO ILLUSTRATE THE USE OF INTERMEDIATE VARIABLES)
template<typename T>
class modelR : virtual public ODE<T> {
public:
	void makeEventTime(const T t, T* parms, T* y, T* x, T h) override {
} 


	void makeEventVar(const T t,T* parms, T* y, T* x, T h) override {
} 


	// GOODWIN-KEEN MODEL DEFINITION
	void Func(const T t, const T* y, const T* parms, T* ydot, T* x) override {

x[0] = this->getExogVar(t, 0.0);
x[1] = this->getExogVar(t, 1.0);
x[2] = this->getExogVar(t, 2.0);
x[3] = this->getExogVar(t, 3.0);
x[4] = this->getExogVar(t, 4.0);
x[5] = this->getExogVar(t, 5.0);
x[6] = this->getExogVar(t, 6.0);
x[7] = this->getExogVar(t, 7.0);
x[8] = this->getExogVar(t, 8.0);
x[9] = this->getExogVar(t, 9.0);
x[10] = this->getExogVar(t, 10.0);
x[11] = this->getExogVar(t, 11.0);
x[12] = this->getExogVar(t, 12.0);
x[13] = this->getExogVar(t, 13.0);
x[14] = this->getExogVar(t, 14.0);
x[15] = this->getExogVar(t, 15.0);
x[16] = this->getExogVar(t, 16.0);
x[17] = this->getExogVar(t, 17.0);
x[18] = this->getExogVar(t, 18.0);
x[19] = this->getExogVar(t, 19.0);
x[20] = this->getExogVar(t, 20.0);
x[21] = this->getExogVar(t, 21.0);
x[22] = this->getExogVar(t, 22.0);
x[23] = this->getExogVar(t, 23.0);
x[24] = this->getExogVar(t, 24.0);
x[25] = this->getExogVar(t, 25.0);
x[26] = this->getExogVar(t, 26.0);
x[27] = this->getExogVar(t, 27.0);
x[28] = this->getExogVar(t, 28.0);
x[29] = this->getExogVar(t, 29.0);
x[30] = this->getExogVar(t, 30.0);
x[31] = this->getExogVar(t, 31.0);
x[32] = this->getExogVar(t, 32.0);
x[33] = this->getExogVar(t, 33.0);
x[34] = this->getExogVar(t, 34.0);
x[35] = this->getExogVar(t, 35.0);
x[36] = this->getExogVar(t, 36.0);
x[37] = this->getExogVar(t, 37.0);
x[38] = this->getExogVar(t, 38.0);
x[39] = this->getExogVar(t, 39.0);
x[40] = this->getExogVar(t, 40.0);
x[41] = this->getExogVar(t, 41.0);
x[42] = this->getExogVar(t, 42.0);
x[43] = this->getExogVar(t, 43.0);
x[44] = this->getExogVar(t, 44.0);
x[45] = this->getExogVar(t, 45.0);
x[46] = this->getExogVar(t, 46.0);
x[47] = this->getExogVar(t, 47.0);
x[48] = this->getExogVar(t, 48.0);
x[49] = this->getExogVar(t, 49.0);
x[50] = this->getExogVar(t, 50.0);
x[51] = this->getExogVar(t, 51.0);
x[73] = parms[1] * y[0];
x[77] = y[31] + y[41];
x[82] = ((1.0/(1.0 + exp(parms[4] * (t - 2019.0) - parms[5]))) * (parms[6] - parms[6] * parms[7]) + parms[6] * parms[7]) + parms[8];
x[90] = (1.0/(1.0 + exp(-parms[208] * ((t - 2019.0) - parms[209])))) * parms[210];
x[107] = parms[219] + parms[220] * pow((y[62]/y[61]), parms[221]);
x[108] = (1.0/(1.0 + exp(parms[30] * (t - 2019.0) - parms[31]))) * (parms[12] - parms[12] * parms[13]) + parms[12] * parms[13];
x[109] = (1.0/(1.0 + exp(parms[30] * (t - 2019.0) - parms[31]))) * (parms[18] - parms[18] * parms[19]) + parms[18] * parms[19];
x[110] = (1.0/(1.0 + exp(parms[30] * (t - 2019.0) - parms[31]))) * (parms[24] - parms[24] * parms[25]) + parms[24] * parms[25];
x[114] = (1.0/(1.0 + exp(parms[38] * (t - 2019.0) - parms[39]))) * (parms[32] - parms[32] * parms[37]) + parms[32] * parms[37];
x[115] = parms[217] * pow((y[3]/y[2]), parms[218]);
x[119] = parms[40] - parms[41] * (y[1]/y[0] - parms[1]);
x[123] = (y[11] * (1.0 - y[7]) + y[63] * y[58] * (1.0 + parms[136]) * y[7]) * (1.0 + parms[140]);
x[125] = (y[11] * (1.0 - y[8]) + y[63] * y[58] * (1.0 + parms[211]) * y[8]) * (1.0 + parms[212]);
x[136] = y[63] * y[58]/y[11];
x[137] = y[63] * y[58];
x[140] = parms[222] * pow((y[3]/y[2]), parms[223]);
x[158] = parms[69] * y[35];
x[159] = parms[70] * y[17];
x[164] = ((1.0/(1.0 + exp(parms[73] * (t - 2019.0) - parms[74]))) * (parms[75] - parms[75] * parms[76]) + parms[75] * parms[76]) + parms[77];
x[171] = parms[84] * (y[17] + y[35] + y[15] * y[58]);
x[175] = 0.0;
x[176] = y[43] + y[34] + y[13];
x[193] = 0.155;
x[201] = 0.0;
x[215] = parms[143] * (y[72] * y[66] * y[58]);
x[223] = parms[148] * y[69];
x[225] = ((1.0/(1.0 + exp(parms[149] * (t - 2019.0) - parms[150]))) * (parms[151] - parms[151] * parms[152]) + parms[151] * parms[152]) + parms[153];
x[226] = parms[154] * y[42];
x[235] = y[30] + y[54];
x[245] = parms[178] * y[68] * y[63];
x[247] = (1.0/(1.0 + exp(parms[179] * (t - 2019.0) - parms[180]))) * (parms[181] - parms[181] * parms[182]) + parms[181] * parms[182];
x[274] = parms[52] * y[59];
x[275] = parms[52] * y[61];
x[276] = parms[53] * y[69];
x[279] = parms[62] * (parms[61] * (y[15] + y[16]) - y[14]);
x[286] = parms[78] * y[18];
x[290] = parms[87] * (parms[86] * y[23] - y[22]);
x[309] = 0.0;
x[318] = parms[167] * (parms[166] * (y[49] + y[47]) - y[45]);
x[331] = parms[188] * y[60];
x[332] = parms[188] * y[62];
x[333] = parms[190] * y[63];
x[334] = parms[191] * y[64];
x[335] = parms[190] * y[65];
x[336] = parms[192] * y[66];
x[337] = parms[193] * y[67];
x[338] = parms[189] * y[68];
ydot[14] = x[279];
ydot[18] = x[286];
ydot[22] = x[290];
ydot[38] = x[309];
ydot[45] = x[318];
ydot[59] = x[274];
ydot[60] = x[331];
ydot[61] = x[275];
ydot[62] = x[332];
ydot[63] = x[333];
ydot[64] = x[334];
ydot[65] = x[335];
ydot[66] = x[336];
ydot[67] = x[337];
ydot[68] = x[338];
ydot[69] = x[276];
ydot[72] = -x[30] * y[72];
x[53] = x[36] * y[2];
x[54] = x[35] * y[2];
x[59] = x[41] * y[18];
x[60] = x[42] * y[18];
x[61] = x[43] * y[18];
x[62] = x[44] * x[223];
x[63] = x[45] * x[223];
x[64] = x[46] * x[223];
x[65] = x[47] * y[32];
x[66] = x[49] * y[32];
x[67] = x[48] * y[32];
x[68] = x[50] * y[32];
x[69] = x[51] * y[32];
x[72] = parms[2] * (x[73] - y[1]);
x[91] = x[90] * parms[207] + y[73];
x[96] = x[12] * x[8];
x[97] = x[13] * x[9];
x[98] = x[14] * x[10];
x[99] = x[15] * x[11];
x[100] = x[17] * x[16];
x[101] = x[19] * x[18];
x[102] = x[21] * x[20];
x[103] = x[23] * x[22];
x[104] = x[108] * pow((y[11]/(y[63] * y[58] * (1.0 + parms[136]))), parms[14]) + parms[15] * pow((y[60]/y[59]), parms[16]);
x[105] = x[109] * pow((y[11]/(y[63] * y[58] * (1.0 + parms[136]))), parms[20]) + parms[21] * pow((y[60]/y[59]), parms[22]);
x[106] = x[110] * pow((y[11]/(y[63] * y[58] * (1.0 + parms[136]))), parms[26]) + parms[27] * pow((y[60]/y[59]), parms[28]);
x[111] = y[72] * y[66] * y[58] + y[9] * y[68] * y[65] * y[58] + x[25] * y[67] * y[58];
x[113] = x[114] * pow((y[65] * y[58]/(y[11] * (1.0 + x[115]))), parms[33]) + parms[34] * (pow((y[59]/y[60]), parms[35]));
x[118] = (1.0 + x[119]) * y[10];
x[126] = y[11] * x[0] * (1.0 - x[12]) + y[63] * y[58] * x[1] * (1.0 + parms[136]) * x[12];
x[127] = y[11] * x[2] * (1.0 - x[13]) + y[63] * y[58] * x[3] * (1.0 + parms[136]) * x[13];
x[128] = y[11] * x[4] * (1.0 - x[14]) + y[63] * y[58] * x[5] * (1.0 + parms[136]) * x[14];
x[129] = y[11] * x[6] * (1.0 - x[15]) + y[63] * y[58] * x[7] * (1.0 + parms[136]) * x[15];
x[130] = y[11] * (1.0 - x[17]) + y[63] * y[58] * x[24] * (1.0 + parms[136]) * x[17];
x[131] = y[11] * (1.0 - x[19]) + y[63] * y[58] * x[24] * (1.0 + parms[136]) * x[19];
x[132] = y[11] * (1.0 - x[21]) + y[63] * y[58] * x[24] * (1.0 + parms[136]) * x[21];
x[133] = y[11] * (1.0 - x[23]) + y[63] * y[58] * x[24] * (1.0 + parms[136]) * x[23];
x[157] = x[158] + x[159];
x[161] = parms[71] * y[32] * x[123];
x[162] = parms[72] * y[2] * x[123];
x[163] = x[164] * y[18];
x[172] = parms[85] * (x[171] - y[27]);
x[179] = parms[88] - parms[89]/(1.0 + exp(-parms[90] * (y[24]/x[176] - parms[91])));
x[190] = x[31] + parms[116];
x[191] = x[31] + parms[117];
x[224] = x[225] * x[223];
x[240] = (1.0 - parms[206]) * x[235];
x[270] = parms[213] * (x[107] - y[8]);
x[305] = y[33]/x[123] - parms[131] * y[32];
x[314] = y[40]/x[123] - parms[155] * y[42];
x[329] = x[279] + x[290] + x[318];
ydot[8] = x[270];
ydot[32] = x[305];
ydot[42] = x[314];
ydot[56] = x[329];
x[71] = y[0] + x[72];
x[83] = x[123] * y[4] + x[126] * x[8];
x[85] = y[40] + x[10] * x[128];
x[86] = y[33] + x[11] * x[129];
x[92] = x[91] * x[125];
x[124] = x[111]/(y[72] + y[9] * y[68] + x[25]);
x[135] = parms[200] * (1.0 - parms[201]) * x[91] * x[125]/x[77];
x[160] = x[161] + x[162];
x[178] = y[30] - x[179];
x[192] = y[30] * y[24] + x[190] * y[57] * y[58] - x[193] * y[44];
x[244] = parms[199] * x[91] * x[125]/y[58];
x[246] = x[247] * (y[4] * x[123] + x[8] * x[126]);
x[266] = x[91] - parms[11] * y[3];
x[267] = parms[17] * (x[104] - y[5]);
x[268] = parms[23] * (x[105] - y[6]);
x[269] = parms[29] * (x[106] - y[7]);
x[271] = parms[36] * (x[113] - y[9]);
x[273] = parms[43] * (x[118] - y[11]);
x[297] = x[172];
x[307] = parms[126] * (y[33] + x[11] * x[129]);
x[322] = parms[202] * parms[203] * x[91] * x[125]/y[58];
x[323] = parms[202] * (1.0 - parms[203]) * x[91] * x[125];
ydot[3] = x[266];
ydot[5] = x[267];
ydot[6] = x[268];
ydot[7] = x[269];
ydot[9] = x[271];
ydot[11] = x[273];
ydot[27] = x[297];
ydot[37] = x[307];
ydot[50] = x[322];
ydot[51] = x[323];
x[57] = x[39] * x[71];
x[79] = parms[3] * x[71];
x[112] = x[111]/x[124];
x[121] = (y[11] * (1.0 - y[5]) + y[63] * y[58] * (1.0 + parms[136]) * y[5]) * (1.0 + parms[137] + parms[138] + x[135]);
x[156] = x[160] + x[157];
x[181] = ((x[178] * y[43] + x[178] * (1.0 - parms[92]) * y[13] + x[178] * (1.0 - parms[93]) * y[34]) + y[30] * y[24])/(x[176] + y[24]);
x[189] = x[33] + parms[113] * (x[273]/y[11] - parms[114]);
x[200] = (1.0/(1.0 + exp(-parms[121] * (x[178] - parms[122] - x[273]/y[11])))) * (parms[123] - parms[124]) + parms[124];
x[248] = parms[183] * x[246];
x[251] = (1.0 - parms[183]) * x[246];
x[287] = (parms[81] * (x[274]/y[59]) + parms[82] * x[273]/y[11]) * y[20];
x[295] = (1.0 - parms[204]) * x[323];
x[315] = (parms[145] * (x[274]/y[59]) + parms[146] * x[273]/y[11]) * y[39];
x[327] = parms[204] * x[323];
ydot[20] = x[287];
ydot[39] = x[315];
ydot[52] = x[327];
ydot[53] = x[295];
x[134] = parms[200] * parms[201] * x[91] * x[125]/((y[11] * (1.0 - y[6]) + y[63] * y[58] * (1.0 + parms[136]) * y[6]) * (1.0 + parms[139]) * (x[79] + x[163] + x[224]));
x[165] = parms[79] * x[156];
x[180] = x[181] * (1.0 + y[28]);
x[211] = parms[137] * x[77] * ((1.0 - y[5]) * y[11] + y[5] * y[63] * y[58] * (1.0 + parms[136]))/x[121];
x[249] = parms[184] * x[248];
x[302] = parms[115] * (x[189] - y[30]);
ydot[30] = x[302];
x[70] = (y[4] + x[249]/x[123])/y[2] - parms[11];
x[80] = x[123] * y[4] + y[33] + x[165] + y[40] + x[249];
x[84] = x[165] + x[127] * x[9];
x[122] = (y[11] * (1.0 - y[6]) + y[63] * y[58] * (1.0 + parms[136]) * y[6]) * (1.0 + parms[139] + x[134]);
x[183] = x[180] * (1.0 + y[29]);
x[250] = x[248] - x[249];
x[265] = y[4] + x[249]/x[123] - parms[11] * y[2];
x[285] = x[165]/x[123] - parms[80] * y[19];
ydot[2] = x[265];
ydot[19] = x[285];
x[78] = x[122] * (x[79] + x[224] + x[163]);
x[87] = x[122] * x[79] + x[130] * x[16];
x[88] = x[122] * x[163] + x[131] * x[18];
x[89] = x[122] * x[224] + x[20] * x[132];
x[168] = x[156] - x[122] * x[163] - x[131] * x[18] - parms[142] * x[156] - (1.0 + parms[83]) * y[20] * y[18];
x[221] = (1.0 + parms[147]) * y[39] * x[223] + x[122] * x[224] + x[132] * x[20] + parms[155] * x[123] * y[42];
x[75] = x[77] + x[22] * x[133] + x[78] + x[16] * x[130] + x[18] * x[131] + x[20] * x[132] + x[80] + x[92] + x[111] + x[8] * x[126] + x[9] * x[127] + x[10] * x[128] + x[11] * x[129];
x[76] = x[77]/x[121] + x[22] + x[78]/x[122] + x[16] + x[18] + x[20] + x[80]/x[123] + x[91] + x[111]/x[124] + x[8] + x[9] + x[10] + x[11];
x[95] = y[5] * (x[77]/x[121]) + y[6] * (x[78]/x[122]) + y[7] * (x[80]/x[123]) + y[8] * x[92]/x[123];
x[212] = parms[138] * x[77] * ((1.0 - y[5]) * y[11] + y[5] * y[63] * y[58] * (1.0 + parms[136]))/x[121] + parms[139] * x[78] * ((1.0 - y[6]) * y[11] + y[6] * y[63] * y[58] * (1.0 + parms[136]))/x[122] + parms[140] * x[80] * ((1.0 - y[7]) * y[11] + y[7] * y[63] * y[58] * (1.0 + parms[136]))/x[123];
x[213] = x[135] * x[77] * ((1.0 - y[5]) * y[11] + y[5] * y[63] * y[58] * (1.0 + parms[136]))/x[121] + x[134] * x[78] * ((1.0 - y[6]) * y[11] + y[6] * y[63] * y[58] * (1.0 + parms[136]))/x[122];
x[220] = x[221] + y[41];
x[74] = x[71] - x[95] - x[96] - x[97] - x[98] - x[99] - x[100] - x[101] - x[102] - x[103];
x[94] = x[95] * y[63] * y[58] + (x[96] * x[1] + x[97] * x[3] + x[98] * x[5] + x[99] * x[7] + x[100] * x[24] + x[101] * x[24] + x[102] * x[24] + x[103] * x[24]) * y[64] * y[58];
x[117] = x[77]/x[121] + x[22] + x[80]/x[123] + x[91] + x[8] + x[9] + x[10] + x[11] + x[112] - x[95] - x[96] - x[97] - x[98] - x[99] - x[100] - x[101] - x[102] - x[103];
x[262] = parms[0] * (x[76] - y[0]) + x[70] * y[0];
x[263] = x[71] - x[76];
ydot[0] = x[262];
ydot[1] = x[263];
x[52] = x[34] * x[74];
x[55] = x[37] * x[74];
x[56] = x[38] * x[74];
x[58] = x[40] * x[74];
x[116] = y[31] + x[22] * x[133] + y[41] + x[158] + x[161] + x[221] + x[80] + x[92] + x[8] * x[126] + x[9] * x[127] + x[10] * x[128] + x[11] * x[129] + x[111] - x[94];
x[139] = x[74]/(y[59]);
x[182] = parms[94] + parms[95]/(1.0 + exp(-parms[96] * ((y[17] + y[15] * y[58] + y[16] * y[58])/y[11] * x[74])));
x[210] = parms[136] * x[94];
x[214] = parms[141] * y[11] * x[74] + parms[142] * x[156];
x[242] = x[111] - x[94];
x[256] = x[32] * pow((x[94]/(y[55] * y[58])), parms[185]);
x[257] = parms[194] * x[74] * y[11];
x[258] = parms[195] * x[74] * y[11];
x[259] = parms[196] * x[74] * y[11];
x[260] = parms[197] * x[74] * y[11];
x[261] = parms[198] * x[74] * y[11];
x[301] = std::max(parms[118] * x[94]/y[58] - y[57], 0.0);
ydot[57] = x[301];
x[93] = (1.0/(1.0 + exp(-parms[214] * ((t - 2019.0) - parms[215])))) * parms[216] * std::max((0.013 * x[116] - x[92])/x[125], 0.0);
x[120] = ((1.0 + parms[51]) * y[12] * x[139] + x[122] * x[79] + x[130] * x[16] + x[26] + parms[141] * y[11] * x[74])/x[74];
x[138] = x[139] + x[223] + y[18];
x[142] = x[75] - x[94] - x[210] - parms[141] * y[11] * x[74] - x[212] - x[211] - x[122] * x[79] - x[130] * x[16] - x[162] - x[159] - (1.0 + parms[51]) * y[12] * x[139];
x[185] = parms[103] + parms[104] * pow((x[256]), parms[102]);
x[195] = y[12] * x[139] + y[39] * x[223] + y[20] * y[18];
x[196] = parms[51] * y[12] * x[139] + parms[147] * y[39] * x[223] + parms[83] * y[20] * y[18];
x[222] = parms[157] * x[116];
x[227] = x[226] * x[123] + parms[224] * x[116];
x[228] = parms[159] * y[12] * (y[69] - x[223] - x[139] - y[18]) + parms[160] * y[12] * y[69];
x[236] = parms[172] + parms[173]/(exp(-parms[174] * ((y[46] + y[47] * y[58] + y[49] * y[58] + y[50] * y[58] + y[51])/x[116])));
x[254] = -(y[55] * y[58] + y[56] * y[58] - y[23] * y[58] - y[16] * y[58] - y[47] * y[58] - y[49] * y[58] - y[50] * y[58] - y[48] - y[52])/x[116];
x[255] = ((y[16] + y[23] + y[47] + y[49] + y[50] - y[56]) * y[58])/x[116];
x[278] = parms[60] * (parms[59] * y[12] * x[139] * (1.0 + parms[51]) - y[13]);
x[283] = 1.0/(1.0 + exp(-parms[65] * (x[256] - parms[68]))) * (parms[66] - parms[67]) + parms[67];
x[293] = 1.0/(1.0 + exp(-parms[108] * (x[256] - parms[111]))) * (parms[109] - parms[110]) + parms[110];
x[299] = parms[97] * (x[182] - y[28]);
x[320] = -parms[171] * (y[71] * x[242]/y[58]);
x[321] = -(1.0 - parms[171]) * (y[71] * x[242]/y[58]);
x[326] = -parms[186] * x[242];
ydot[13] = x[278];
ydot[28] = x[299];
ydot[47] = x[320];
ydot[48] = x[326];
ydot[49] = x[321];
ydot[73] = 2.0 * (x[93] - y[73]);
x[141] = 1.0 - x[138]/y[69];
x[143] = parms[44] * x[142];
x[144] = parms[45] * x[142];
x[145] = parms[46] * (x[142]);
x[166] = (1.0 - parms[161]) * x[228];
x[186] = x[31] + x[185];
x[188] = x[31] + parms[105] * x[185];
x[197] = x[196] + parms[119] * x[195];
x[229] = parms[161] * x[228];
x[237] = x[31] + parms[176] * x[185];
x[272] = parms[42] * (x[120] - y[10]);
x[277] = (parms[47] * (x[274]/y[59]) + parms[48] * (x[138]/y[69] - parms[49]) + parms[50] * x[273]/y[11]) * y[12];
x[310] = parms[132] * x[195];
x[312] = parms[158] * (x[222] - y[41]);
x[313] = parms[156] * (x[227] - y[40]);
x[325] = parms[175] * (x[236] - y[54]);
ydot[10] = x[272];
ydot[12] = x[277];
ydot[36] = x[310];
ydot[40] = x[313];
ydot[41] = x[312];
ydot[54] = x[325];
x[167] = (1.0 - parms[144]) * x[197];
x[187] = x[186] * (1.0 + parms[106] * y[28]);
x[204] = parms[127] - parms[128] * x[183] - parms[129] * x[141];
x[216] = parms[144] * x[197];
x[218] = x[220] + (1.0 + parms[147]) * y[39] * x[223] + x[122] * x[224] + x[132] * x[20] + y[40] + x[10] * x[128] + x[91] * x[125] + x[229];
x[238] = (1.0 - parms[177]) * x[237];
x[146] = x[142] - x[215] - x[180] * y[17] - x[187] * y[15] * y[58] - x[188] * y[16] * y[58] + x[178] * (1.0 - parms[92]) * y[13] - (x[145] + x[143] + x[144]);
x[169] = x[183] * y[35] + x[180] * y[17] + x[187] * y[15] * y[58] + x[235] * y[25] + y[53] * x[240] - (x[178] * y[43] + x[178] * (1.0 - parms[92]) * y[13] + x[178] * (1.0 - parms[93]) * y[34]) - x[186] * y[23] * y[58] + x[191] * y[21] * y[58] - y[30] * y[24] - x[122] * x[163] - x[131] * x[18] - parms[142] * x[156] - (1.0 + parms[83]) * y[20] * y[18] + x[167] - x[166] + x[160] + x[157];
x[239] = (1.0 - parms[205]) * x[238];
x[147] = (1.0 - parms[133]) * x[146];
x[170] = (1.0 - parms[134]) * x[169];
x[209] = parms[135] * x[195] + parms[133] * x[146] + parms[134] * x[169];
x[219] = x[235] * y[46] + x[237] * y[47] * y[58] + x[238] * y[49] * y[58] + y[50] * x[239] * y[58] + y[51] * x[240];
x[148] = x[147] - x[279] * y[58] - x[278];
x[149] = x[147]/(x[123] * y[2]);
x[173] = x[170] - x[172] - x[258];
x[208] = x[209] + x[210] + x[211] + x[212] + x[213] + x[214];
x[217] = x[218] + x[219];
x[81] = (x[82] + parms[9] * (x[149] - x[273]/y[11])) * y[2];
x[150] = (1.0 - parms[58]) * x[148];
x[154] = parms[58] * x[148] - x[257];
x[174] = x[173];
x[232] = parms[162] * x[217];
x[233] = parms[164] * x[217];
x[151] = std::max(0.0, (parms[54] + parms[55] * (y[72] * y[66])/(x[116]/y[58])) * x[150]);
x[152] = std::max(0.0, (parms[56] + parms[57] * (y[72] * y[66])/(x[116]/y[58])) * x[150]);
x[155] = x[123] * y[4] + x[126] * x[8] - x[154];
x[264] = parms[10] * (x[81] - y[4]);
x[316] = parms[163] * (x[232] - y[43]);
x[317] = parms[165] * (x[233] - y[44]);
ydot[4] = x[264];
ydot[43] = x[316];
ydot[44] = x[317];
x[153] = x[150] - x[151] - x[152];
x[207] = x[208] + x[215] + x[144] + x[216] + x[178] * y[43] + x[193] * y[44] + x[152] - x[259] + x[192];
x[243] = (x[245] + x[190] * y[57] + x[191] * y[21] + x[244] - x[239] * y[50] - x[237] * y[47] - x[238] * y[49] - x[186] * y[23] - x[188] * y[16]) * y[58] - x[151] - x[175] + x[261] - x[235] * y[48] - y[52] * x[240];
x[280] = parms[63] * (x[155]/y[58]);
x[282] = (1.0 - x[283]) * parms[64] * (x[155]/y[58]);
ydot[16] = x[282];
x[194] = (1.0 - parms[135]) * x[195] + x[145] + x[196] + x[228] - x[197] - x[183] * y[35] + x[178] * (1.0 - parms[93]) * y[34] + x[153] + x[174] + x[245] * y[58] + x[143] - x[161] - x[158] + x[260];
x[230] = x[217] - x[207] - x[221];
x[241] = -(x[242] + x[243])/x[116];
x[281] = (1.0 - x[293]) * x[280];
x[291] = (parms[107] * x[297]/y[58] + x[280]);
ydot[15] = x[281];
x[184] = parms[98] + parms[99]/(1.0 + exp(-parms[100] * (y[35]/x[194])));
x[202] = y[38] * x[194];
x[203] = x[204] * x[194];
x[205] = x[194] - y[31] - x[22] * x[133];
x[231] = x[230] + x[316] + x[317] + x[318] * y[58];
x[234] = parms[168] + parms[169] * x[241];
x[284] = x[155] - x[281] * y[58] - x[282] * y[58] - x[250];
x[288] = x[291] - x[290] - x[281];
x[292] = (1.0 - x[293]) * x[291];
ydot[17] = x[284];
ydot[23] = x[292];
x[206] = y[33] + x[11] * x[129] - x[205];
x[252] = x[94]/y[58] + x[237] * y[47] + x[238] * y[49] + x[186] * y[23] + x[188] * y[16] + x[239] * y[50] + x[151]/y[58] + x[175]/y[58] + x[288] + x[329] + x[235] * y[48]/y[58] + y[52] * x[240]/y[58];
x[253] = x[111]/y[58] + x[245] + x[261]/y[58] + x[190] * y[57] + x[191] * y[21] + x[246]/y[58] + x[320] + x[321] + x[282] + x[292] + x[322] + x[244] + x[326]/y[58] + x[327]/y[58] - x[301];
x[300] = parms[101] * (x[184] - y[29]);
x[304] = parms[130] * (x[203] - y[33]);
x[308] = parms[125] * (x[202] - y[70]);
x[319] = parms[170] * (x[234] - y[71]);
x[324] = x[231] - x[320] * y[58] - x[321] * y[58] - x[322] * y[58] - x[323] - parms[199] * x[91] * x[125]/y[58];
x[328] = (x[242]/y[58] + x[243]/y[58] + x[246]/y[58] + x[320] + x[326]/y[58] + x[321] + x[282] + x[292] + x[322] + x[244] - x[329]);
ydot[29] = x[300];
ydot[33] = x[304];
ydot[46] = x[324];
ydot[55] = x[328];
ydot[70] = x[308];
ydot[71] = x[319];
x[198] = x[200] * x[194] + x[201] * (y[34] + y[36]) + x[308];
x[289] = x[328] - x[301];
x[294] = x[324] - x[326];
x[306] = x[308] + x[307];
x[330] = parms[187] * ((x[252] - x[253])/x[253]);
ydot[21] = x[289];
ydot[25] = x[294];
ydot[35] = x[306];
ydot[58] = x[330];
x[199] = x[198] - x[22] * x[133];
x[311] = x[205] - y[33] - x[11] * x[129] + x[306] - x[310];
ydot[34] = x[311];
x[177] = (x[284] + x[306] + x[294] + x[295]) + x[165] + x[9] * x[127] + parms[112] * (x[316] + x[311] + x[278]) - (x[316] + x[311] + x[278] + x[297] + x[251]) - x[310] + (x[290] * y[58] + x[281] * y[58] - x[292] * y[58] + x[289] * y[58]);
x[296] = parms[112] * ((x[316] + x[311] + x[278]));
x[303] = parms[120] * (x[199] - y[31]);
ydot[26] = x[296];
ydot[31] = x[303];
x[298] = std::max(x[177], -y[24]);
ydot[24] = x[298];
}	
};

#endif