import os
import time

import numpy as np
import pandas as pd
import pytest

import FINE as fn


@pytest.mark.parametrize("indirect_watersupply_esM", [1], indirect=True)
def test_watersupply(indirect_watersupply_esM):

    # read in original results
    results = pd.read_csv(os.path.join(os.path.dirname(__file__),'..','examples','WaterSupplySystem','totalTransmission.csv'), 
                        index_col = [0,1,2], squeeze=True)


    starttime = time.time()

    esM = indirect_watersupply_esM

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

# Variant 0: using fixture + parametrizing others variables
@pytest.mark.parametrize("indirect_watersupply_esM", [1], indirect=True)
@pytest.mark.parametrize("additional_variable, expected", [(1, 1), (2, 2), (3, 3)])
def test_watersupply_with_additional_variables(indirect_watersupply_esM, additional_variable, expected):

    # read in original results
    results = pd.read_csv(os.path.join(os.path.dirname(__file__),'..','examples','WaterSupplySystem','totalTransmission.csv'), 
                        index_col = [0,1,2], squeeze=True)


    starttime = time.time()

    esM = indirect_watersupply_esM

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


@pytest.mark.parametrize("indirect_watersupply_esM", [0, 1, 2] , indirect=["indirect_watersupply_esM"])
def test_watersupply_indirect_parametrization(indirect_watersupply_esM):
    # # Optimize the system
    indirect_watersupply_esM.cluster(numberOfTypicalPeriods=7)
