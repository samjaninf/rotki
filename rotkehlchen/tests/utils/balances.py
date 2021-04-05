from rotkehlchen.assets.asset import Asset
from rotkehlchen.constants.assets import A_BTC, A_ETH
from rotkehlchen.constants.misc import ZERO
from rotkehlchen.fval import FVal
from rotkehlchen.tests.utils.rotkehlchen import BalancesTestSetup
from rotkehlchen.utils.misc import from_wei, satoshis_to_btc


def get_asset_balance_total(asset: Asset, setup: BalancesTestSetup) -> FVal:
    conversion_function = satoshis_to_btc if asset == A_BTC else from_wei
    total = ZERO

    if asset in (A_ETH, A_BTC):
        asset_balances = getattr(setup, f'{asset.symbol.lower()}_balances')
        total += sum(conversion_function(FVal(b)) for b in asset_balances)
    elif asset.is_eth_token():
        asset_balances = setup.token_balances[asset]  # type: ignore
        total += sum(conversion_function(FVal(b)) for b in asset_balances)

    total += setup.binance_balances.get(asset, ZERO)
    total += setup.poloniex_balances.get(asset, ZERO)

    if setup.manually_tracked_balances:
        for entry in setup.manually_tracked_balances:
            if entry.asset == asset:
                total += entry.amount

    return total
