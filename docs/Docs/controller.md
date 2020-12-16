# （準備中）コントローラについて

## controller

[controller.m]()

全てのコントローラクラスの基底クラス．  

## controller_broadcast_PI

[controller_broadcast_PI.m]()

ブロードキャストコントローラ（PIコントローラ）の実装．  
周波数偏差をフィードバックする．


## controller_broadcast_PI_AGC

[controller_broadcast_PI_AGC.m]()

ブロードキャストAGCの実装．


## controller_broadcast_PI_AGC_normal

[controller_broadcast_PI_AGC_normal.m]()

ブロードキャストAGCの実装．  
[controller_broadcast_PI_AGC_normal](/Docs/controller/#controller_broadcast_pi_agc_normal)との違いは，ゲインを電力に比例した形にしていること．


## controller_LQR

[controller_LQR.m]()

あるバスに対するLQRの実装．


## controller_retrofit_generator

[controller_retrofit_generator.m]()

全てのレトロフィットコントローラクラスの基底クラス．


### controller_retrofit_generator_nonlinear

[controller_retrofit_generator_nonlinear.m]()


#### controller_retofit_type1

[controller_retrofit_type1.m]()


### controller_retrofit_generator_nonlinear_AGC_LQR

[controller_retrofit_generator_nonlinear_AGC_LQR]()


### controller_retrofit_generator_nonlinear_UKF

[controller_retrofit_generator_nonlinear_UKF.m]()


#### controller_retrofit_generator_nonlinear_AGC_LQR_UKF

[controller_retrofit_generator_nonlinear_AGC_LQR_UKF.m]()

