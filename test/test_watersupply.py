import os
import time

import pandas as pd
import numpy as np

import FINE as fn

import pytest


def test_watersupply(watersupply_esM_1):

    # read in original results
    results = pd.read_csv(os.path.join(os.path.dirname(__file__),'..','examples','WaterSupplySystem','totalTransmission.csv'), 
                        index_col = [0,1,2], squeeze=True)


    starttime = time.time()

    esM = watersupply_esM_1

    # # Optimize the system
    esM.cluster(numberOfTypicalPeriods=7)
    esM.optimize(timeSeriesAggregation=True, solver = 'glpk', optimizationSpecs='LogToConsole=1 OptimalityTol=1e-6 crossover=1')


    # # Selected results output
    esM.getOptimizationSummary("SourceSinkModel", outputLevel=2)


    # ### Storage
    esM.getOptimizationSummary("StorageModel", outputLevel=2)


    # ### Transmission
    esM.getOptimizationSummary("TransmissionModel", outputLevel=2)
    esM.componentModelingDict["TransmissionModel"].operationVariablesOptimum.sum(axis=1)

    #
    testresults = esM.componentModelingDict["TransmissionModel"].operationVariablesOptimum.sum(axis=1)

    print('Optimization took ' + str(time.time() - starttime))


    # test if here solved fits with original results
    # np.testing.assert_array_almost_equal(testresults.values[:-1], results.values,decimal=1)

# Variant 0: using fixture + parametrizing other variables
@pytest.mark.parametrize("additional_variable, expected", [(1, 1), (2, 2), (3, 3)])
def test_watersupply_with_additional_variables(watersupply_esM_1, additional_variable, expected):

    # read in original results
    results = pd.read_csv(os.path.join(os.path.dirname(__file__),'..','examples','WaterSupplySystem','totalTransmission.csv'), 
                        index_col = [0,1,2], squeeze=True)


    starttime = time.time()

    esM = watersupply_esM_1

    # # Optimize the system
    esM.cluster(numberOfTypicalPeriods=7)
    esM.optimize(timeSeriesAggregation=True, solver = 'glpk', optimizationSpecs='LogToConsole=1 OptimalityTol=1e-6 crossover=1')


    # # Selected results output
    esM.getOptimizationSummary("SourceSinkModel", outputLevel=2)


    # ### Storage
    esM.getOptimizationSummary("StorageModel", outputLevel=2)


    # ### Transmission
    esM.getOptimizationSummary("TransmissionModel", outputLevel=2)
    esM.componentModelingDict["TransmissionModel"].operationVariablesOptimum.sum(axis=1)

    #
    testresults = esM.componentModelingDict["TransmissionModel"].operationVariablesOptimum.sum(axis=1)

    print('Optimization took ' + str(time.time() - starttime))

    assert additional_variable == expected

    # test if here solved fits with original results
    # np.testing.assert_array_almost_equal(testresults.values[:-1], results.values,decimal=1)


# Variant 1: my initial thought - parametrizing fixtures
# @pytest.mark.parametrize("esM", [watersupply_esM_1, watersupply_esM_2, watersupply_esM_3])
# def test_watersupply_parametrize_fixtures(esM):
def test_watersupply_parametrize_fixtures(watersupply_esM_1):

    # read in original results
    results = pd.read_csv(os.path.join(os.path.dirname(__file__),'..','examples','WaterSupplySystem','totalTransmission.csv'), 
                          index_col = [0,1,2], squeeze=True)

    starttime = time.time()

    # # Optimize the system
    esM.cluster(numberOfTypicalPeriods=7)
    esM.optimize(timeSeriesAggregation=True, solver = 'glpk', optimizationSpecs='LogToConsole=1 OptimalityTol=1e-6 crossover=1')


    # # Selected results output
    esM.getOptimizationSummary("SourceSinkModel", outputLevel=2)


    # ### Storage
    esM.getOptimizationSummary("StorageModel", outputLevel=2)


    # ### Transmission
    esM.getOptimizationSummary("TransmissionModel", outputLevel=2)
    esM.componentModelingDict["TransmissionModel"].operationVariablesOptimum.sum(axis=1)

    #
    testresults = esM.componentModelingDict["TransmissionModel"].operationVariablesOptimum.sum(axis=1)

    print('Optimization took ' + str(time.time() - starttime))


    # test if here solved fits with original results
    # np.testing.assert_array_almost_equal(testresults.values, results.values,decimal=2)


# Variant 2: fixture.param - defining a fixture that has attribute param to select which object to use
@pytest.mark.skip("Not yet implemented")
def test_watersupply_fixture_param():
    pass


# Variant 3: use indirection https://docs.pytest.org/en/latest/example/parametrize.html#apply-indirect-on-particular-arguments
# @pytest.mark.skip("Not yet implemented")
@pytest.mark.parametrize("indirect_watersupply_esM", [0, 1, 2] , indirect=True)
def test_watersupply_indirect_parametrization(indirect_watersupply_esM):
    # # Optimize the system
    indirect_watersupply_esM.cluster(numberOfTypicalPeriods=7)

    

# Variant 4: pytest-lazy-fixture
@pytest.mark.skip("Not yet implemented")
def test_watersupply_lazy_parametrization():
    pass
