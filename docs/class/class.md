# クラス定義

- [Power Network](./PowerNetwork/power_network.md)  
    ネットワークの基礎クラス
    - [network_9bus](./PowerNetwork/network_9bus.md)
    - [network_68bus](./PowerNetwork/network_68bus.md)
    - [network_68bus_AGC_const_power1](./PowerNetwork/network_68bus_AGC_const_power1.md)
    - [network_68bus_AGC_varying_impedance](./PowerNetwork/network_68bus_AGC_varying_impedance.md)
    - [network_68bus_const_power1](./PowerNetwork/network_68bus_const_power1.md)
    - [network_68bus_const_power2](./PowerNetwork/network_68bus_const_power2.md)
    - [network_70bus](./PowerNetwork/network_70bus.md)
    - [network_70bus_const_power1](./PowerNetwork/network_70bus_const_power1.md)

- [Bus](./Bus/bus.md)  
    バスの基礎クラス
    - [bus_non_unit](./Bus/bus_non_unit.md)
    - [bus_PQ](./Bus/bus_PQ.md)
    - [bus_PV](./Bus/bus_PV.md)
    - [bus_slack](./Bus/bus_slack.md)

- [Component](./Component/component.md)  
    バスに接続される機器の基礎クラス
    - [component_empty](./Component/component_empty.md)
    - [generator_AGC](./Component/GeneratorAGC/generator_AGC.md)
        - [generator](./Component/GeneratorAGC/generator.md)
    - [load_varying_impedance](./Component/LoadVaryingImpedance/load_varying_impedance.md)
        - [load_const_impedance](./Component/LoadVaryingImpedance/load_const_impedance.md)
    - [load_varying_power](./Component/LoadVaryingPower/load_varying_power.md)
        - [load_const_power](./Component/LoadVaryingPower/load_const_power.md)
    - [solar_farm](./Component/solar_farm.md)
    - [wind_farm](./Component/wind_farm.md)

- [Controller](./Controller/controller.md)  
  コントローラの基礎クラス
    - [controller_broadcast_PI](./Controller/controller_broadcast_PI.md)
    - [controller_broadcast_PI_AGC](./Controller/controller_broadcast_PI_AGC.md)
    - [controller_broadcast_PI_AGC_normal](./Controller/controller_broadcast_PI_AGC_normal.md)
    - [controller_LQR](./Controller/controller_LQR.md)
    - [controller_retrofit_generator](./Controller/ControllerRetrofitGenerator/controller_retrofit_generator.md)
        - [controller_retrofit_generator_nonlinear](./Controller/ControllerRetrofitGenerator/ControllerRetrofitGeneratorNonlinear/controller_retrofit_generator_nonlinear.md)
            - [controller_retrofit_type1](./Controller/ControllerRetrofitGenerator/ControllerRetrofitGeneratorNonlinear/controller_retrofit_type1.md)
        - [controller_retrofit_generator_nonlinear_AGC_LQR](./Controller/ControllerRetrofitGenerator/controller_retrofit_generator_nonlinear_AGC_LQR.md)
        - [controller_retrofit_generator_UKF](./Controller/ControllerRetrofitGenerator/ControllerRetrofitGeneratorUKF/controller_retrofit_generator_UKF.md)
            - [controller_retrofit_generator_nonlinear_AGC_LQR_UKF](./Controller/ControllerRetrofitGenerator/ControllerRetrofitGeneratorUKF/controller_retrofit_generator_nonlinear_AGC_LQR_UKF.md)

- [GenSS](./GenSS/gen_ss.md)  
    システム同定の基礎クラス
    - [gen_ss_diagcat](./GenSS/gen_ss_diagcat.md)
    - [gen_ss_generator_file](./GenSS/gen_ss_generator_file.md)
    - [gen_ss_power_area](./GenSS/gen_ss_power_area.md)
    - [gen_ss_sym_file](./GenSS/gen_ss_sym_file.md)

- [Retrofit](./Retrofit/Retrofit.md)  
  レトロフィットコントローラのクラス
