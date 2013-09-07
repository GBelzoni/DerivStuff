/*
 * ArrearPricer_test.cpp
 *
 *  Created on: Sep 7, 2013
 *      Author: phcostello
 */
// analytic pricer

//product - NPV member

// in arrears fra

// in arrears caplet

// numerical integrator

// model 1 rate

//Classes
// product - base
// - eval method

// fra
// * payoff - forward - strike
// * rate time = T_1 - T_2
// * evolution time, T_2

// arrears fra

//etc

//arrears_pricing_engine(curve, vol , random_gen, stepping_method)

//test price in analytic price of in arrears fra

//test in arrears fra, caplet

//test model - model( curve, vol)
// model.fit(T_1, T_2)

// product(Pay off, Evolution)

// random_gen = random_generator

// mc_pricing_engine(model, random_generator, stepping_method,max_num_path,tol)
// * stop tol ?
// * pricing_engine.eval(results)

// product.eval(pe, statistics)

//fra.eval(analytic, result) /
//fra.eval(mc_bgm, result)

// functional
//fra_anal_price( Strike, Spot, T_1, T_2)
//fra_anal_arr( Strike, Spot, T_1, T_2, vol)
//caption_anal_price( Strike, Spot, T_2, T_2, vol)
//fra_numerical_int( Strike, Spot, T_1, T_2)
//fra_arrears_int( Strike, Spot, vol, T_1, T_2)
//caption_numerical_int( Strike, Spot, vol, T_1, T_2)
//fra_mc_price( Strike, T_1, T_2, vol, random_gen_stepping, max_num, tol, use_tol, results)
//fra_mc_arrears( Strike, T_1, T_2, vol, random_gen_stepping, max_num, tol, use_tol, results)
//caption_mc_arrears( Strike, T_1, T_2, vol, random_gen_stepping, max_num, tol, use_tol, results)

// define loop num_path
// stepping num
