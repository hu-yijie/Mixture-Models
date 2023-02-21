from Mixture_Models import *
from tests import utils


def init_MFA():
    return utils.init_MM(MFA,default_pinwheel_data,10,
    init_params_args={'num_components':3,'q':1, 'scale':0.5}, # q is the latent subspace
    expected={'log proportions': [0.66579325, 0.35763949, -0.77270015], 'means': [[-0.00419192, 0.31066799], [-0.36004278, 0.13275579], [0.05427426, 0.00214572]], 'fac_loadings': [[[0.40631048], [0.30626303]], [[0.36087766], [0.14593803]], [[0.45888706], [0.35728789]]], 'error': [[-0.08730011, -0.56830111], [0.06756844, 0.7422685], [-0.53990244, -0.98886414]]})
    
def check_mpkls(MM,params_store,expected):
    actual = []
    for params in params_store:
        kl_cov = []
        for log_proportion, mean, cov_sqrt, error in zip(*MM.unpack_params(params)):
            kl_cov.append((cov_sqrt@ cov_sqrt.T) + (np.diag(error)@np.diag(error)))
        actual.append(MM.print_mpkl(params['means'],kl_cov))
    utils.check_array_equal(actual,expected)

def test_mfa_illustration():
    test_MFA, init_params = init_MFA()
    params_store = utils.check_fit(test_MFA,init_params,"grad_descent",{'learning_rate':0.0009,'mass':0.95,'maxiter':100},
    100,{'likelihood':[-820.92865287, -794.99234554, -756.81255405, -721.00823406,
       -694.82285344, -678.74675648, -670.49906129, -667.5876386 ,
       -668.02771335, -670.41807324, -673.82878871, -677.65906202,
       -681.52541205, -685.18564561, -688.48954513, -691.34716013,
       -693.7082544 , -695.54877827, -696.86179723, -697.65128301,
       -697.92776737, -697.70522083, -696.99873921, -695.82275471,
       -694.18956549, -692.10801773, -689.58218575, -686.60988795,
       -683.18085442, -679.27433696, -674.85594714, -669.87357592,
       -664.25250946, -657.89053104, -650.65519283, -642.38760823,
       -632.9189665 , -622.10540444, -609.89196902, -596.48362334,
       -582.85626228, -571.49991626, -565.44420693, -564.06018456,
       -561.74766518, -554.91701404, -541.94779049, -533.1436225 ,
       -523.2821485 , -515.4459523 , -539.80459903, -527.02882913,
       -532.05633673, -534.35265124, -539.49726407, -547.61726598,
       -551.10321574, -548.82271268, -554.46313478, -540.0113792 ,
       -536.3931501 , -534.01541819, -529.30231991, -522.77274979,
       -515.72080145, -509.3482739 , -503.10929654, -492.32765482,
       -476.01094429, -466.3253383 , -491.86653002, -478.99618412,
       -458.1594426 , -458.02027532, -459.05437298, -458.0291407 ,
       -462.91434292, -468.68778988, -471.14512756, -470.38644394,
       -469.53075881, -464.55093921, -447.21579923, -439.21363028,
       -443.02037318, -444.36756968, -439.16404587, -438.16619596,
       -441.02224291, -447.93032957, -451.14855511, -447.29726357,
       -443.27416216, -442.19571134, -444.04578985, -443.39019615,
       -441.11701717, -437.04764334, -433.58162407, -431.54276412],
    'aic':[1665.85730575, 1613.98469107, 1537.62510811, 1466.01646813,
       1413.64570687, 1381.49351296, 1364.99812258, 1359.17527719,
       1360.0554267 , 1364.83614648, 1371.65757742, 1379.31812404,
       1387.05082411, 1394.37129121, 1400.97909026, 1406.69432027,
       1411.41650881, 1415.09755654, 1417.72359445, 1419.30256601,
       1419.85553474, 1419.41044165, 1417.99747842, 1415.64550941,
       1412.37913097, 1408.21603546, 1403.1643715 , 1397.21977591,
       1390.36170883, 1382.54867392, 1373.71189427, 1363.74715183,
       1352.50501891, 1339.78106208, 1325.31038565, 1308.77521645,
       1289.837933  , 1268.21080888, 1243.78393803, 1216.96724669,
       1189.71252457, 1166.99983252, 1154.88841386, 1152.12036912,
       1147.49533037, 1133.83402807, 1107.89558099, 1090.28724501,
       1070.564297  , 1054.8919046 , 1103.60919805, 1078.05765825,
       1088.11267346, 1092.70530249, 1102.99452815, 1119.23453195,
       1126.20643148, 1121.64542536, 1132.92626956, 1104.0227584 ,
       1096.78630021, 1092.03083637, 1082.60463982, 1069.54549958,
       1055.4416029 , 1042.6965478 , 1030.21859309, 1008.65530963,
        976.02188858,  956.65067661, 1007.73306004,  981.99236823,
        940.3188852 ,  940.04055064,  942.10874596,  940.05828141,
        949.82868584,  961.37557976,  966.29025511,  964.77288788,
        963.06151763,  953.10187843,  918.43159845,  902.42726057,
        910.04074637,  912.73513936,  902.32809174,  900.33239192,
        906.04448582,  919.86065914,  926.29711021,  918.59452713,
        910.54832432,  908.39142269,  912.0915797 ,  910.7803923 ,
        906.23403434,  898.09528668,  891.16324813,  887.08552824],
    'bic':[1710.30269544, 1658.43008077, 1582.07049781, 1510.46185782,
       1458.09109657, 1425.93890265, 1409.44351228, 1403.62066689,
       1404.50081639, 1409.28153617, 1416.10296712, 1423.76351374,
       1431.49621381, 1438.81668091, 1445.42447995, 1451.13970996,
       1455.8618985 , 1459.54294623, 1462.16898415, 1463.74795571,
       1464.30092443, 1463.85583135, 1462.44286812, 1460.09089911,
       1456.82452067, 1452.66142515, 1447.6097612 , 1441.66516561,
       1434.80709853, 1426.99406362, 1418.15728397, 1408.19254153,
       1396.95040861, 1384.22645178, 1369.75577535, 1353.22060615,
       1334.28332269, 1312.65619857, 1288.22932773, 1261.41263638,
       1234.15791426, 1211.44522221, 1199.33380356, 1196.56575882,
       1191.94072006, 1178.27941777, 1152.34097068, 1134.7326347 ,
       1115.00968669, 1099.33729429, 1148.05458775, 1122.50304795,
       1132.55806316, 1137.15069218, 1147.43991784, 1163.67992165,
       1170.65182118, 1166.09081505, 1177.37165925, 1148.46814809,
       1141.2316899 , 1136.47622607, 1127.05002952, 1113.99088928,
       1099.8869926 , 1087.1419375 , 1074.66398278, 1053.10069933,
       1020.46727828, 1001.0960663 , 1052.17844973, 1026.43775793,
        984.7642749 ,  984.48594033,  986.55413565,  984.5036711 ,
        994.27407553, 1005.82096945, 1010.73564481, 1009.21827757,
       1007.50690732,  997.54726812,  962.87698815,  946.87265027,
        954.48613606,  957.18052906,  946.77348144,  944.77778161,
        950.48987552,  964.30604884,  970.74249991,  963.03991683,
        954.99371401,  952.83681238,  956.53696939,  955.225782  ,
        950.67942403,  942.54067637,  935.60863783,  931.53091794]})
    check_mpkls(test_MFA,params_store,[9.70169098e-01, 7.92992662e-01, 5.60941430e-01, 3.66445032e-01,
       2.68486579e-01, 2.06449776e-01, 1.63070982e-01, 1.29080078e-01,
       9.90362944e-02, 8.25583727e-02, 1.30356752e-01, 1.79406808e-01,
       2.29882424e-01, 2.81643950e-01, 3.34416197e-01, 3.87886306e-01,
       4.41755905e-01, 4.95767411e-01, 5.49715898e-01, 6.03452964e-01,
       6.56886084e-01, 7.09975150e-01, 7.62726664e-01, 8.15185133e-01,
       8.67420366e-01, 9.19508269e-01, 9.71501213e-01, 1.02338151e+00,
       1.07498710e+00, 1.12589045e+00, 1.17519694e+00, 1.22120066e+00,
       1.26078037e+00, 1.28830708e+00, 1.29359937e+00, 1.25793882e+00,
       1.14590663e+00, 1.65610210e+00, 2.64232727e+00, 4.46920250e+00,
       8.18247163e+00, 1.66604233e+01, 3.80575935e+01, 8.41903596e+01,
       1.06651936e+02, 7.68494537e+01, 4.77105813e+01, 3.42685862e+01,
       4.55879137e+01, 2.13836731e+02, 1.34363751e+03, 5.61763115e+01,
       4.25572084e+01, 5.46797482e+01, 7.74373239e+01, 1.19979912e+02,
       1.94516609e+02, 2.94285975e+02, 3.23456271e+02, 1.86464546e+02,
       1.12576604e+02, 8.00453602e+01, 6.52947320e+01, 5.98735623e+01,
       6.08127239e+01, 6.72235500e+01, 7.85176279e+01, 9.32015762e+01,
       1.11645351e+02, 1.72978551e+02, 6.85642248e+02, 3.28529739e+02,
       1.87554638e+02, 1.61436531e+02, 1.45414020e+02, 1.66283876e+02,
       1.93667386e+02, 1.86882718e+02, 1.49014331e+02, 1.20623603e+02,
       1.17018460e+02, 1.46900342e+02, 2.38583505e+02, 4.85639377e+02,
       7.45747571e+02, 4.11533386e+02, 2.26240945e+02, 1.59262676e+02,
       1.41452015e+02, 1.49869771e+02, 1.73914450e+02, 1.99156991e+02,
       2.20986212e+02, 2.54849265e+02, 3.04579419e+02, 3.32445773e+02,
       3.30724030e+02, 3.09474309e+02, 2.75050354e+02, 2.31884805e+02])
    utils.check_labels(test_MFA,default_pinwheel_data,params_store,[0, 0, 0, 0, 2, 2, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 2, 2, 0, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 0,
       2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 0, 0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 0, 0, 2,
       2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
       1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1,
       0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1,
       0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1,
       1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])