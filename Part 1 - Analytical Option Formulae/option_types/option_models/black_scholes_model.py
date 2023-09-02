"""
Authors     : Andre Lim & Joseph Adhika
Tests       : option_types.test_option_models.test_black_76_model
Description : uses lognormal distribution of returns, strictly prices non-zero values
"""
from .abstract_option_model import AbstractOptionModel
import numpy as np
from scipy.stats import norm

class AbstractBlackScholesModel(AbstractOptionModel):
    def __init__(self, S: float, K: float, r: float, sigma: float, T: float):
        self.S = S
        self.K = K
        self.r = r
        self.sigma = sigma
        self.T = T

        self.d1 = self._calculate_d1()
        self.d2 = self._calculate_d2()

    def _calculate_d1(self) -> float:
        return (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma**2) * self.T) / (self.sigma * np.sqrt(self.T))

    def _calculate_d2(self) -> float:
        return self.d1 - self.sigma * np.sqrt(self.T)


class VanillaBlackScholesModel(AbstractBlackScholesModel):
    def calculate_call_price(self) -> float:
        return self.S * norm.cdf(self.d1) - self.K * np.exp(-self.r * self.T) * norm.cdf(self.d2)

    def calculate_put_price(self) -> float:
        return self.K * np.exp(-self.r * self.T) * norm.cdf(-self.d2) - self.S * norm.cdf(-self.d1)


class DigitalCashOrNothingBlackScholesModel(AbstractBlackScholesModel):
    def calculate_call_price(self) -> float:
        pass  # TODO: add formulae

    def calculate_put_price(self) -> float:
        pass  # TODO: add formulae


class DigitalAssetOrNothingBlackScholesModel(AbstractBlackScholesModel):
    def calculate_call_price(self) -> float:
        pass  # TODO: add formulae

    def calculate_put_price(self) -> float:
        pass  # TODO: add formulae
