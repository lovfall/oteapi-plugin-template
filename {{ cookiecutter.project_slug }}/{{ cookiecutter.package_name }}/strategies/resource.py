# pylint: disable=W0511, W0613
"""
Demo resource strategy class
"""
from dataclasses import dataclass
from typing import Any, Dict, Optional

from oteapi.models.resourceconfig import ResourceConfig
from oteapi.plugins.factories import StrategyFactory
from oteapi.plugins.factories import create_download_strategy


@dataclass
@StrategyFactory.register(("accessService", "DEMO-access-service"))
class DemoResourceStrategy:
    """Resource Interface"""

    resource_config: ResourceConfig

    def initialize(self, session: Optional[Dict[str, Any]] = None) -> Dict:
        """Initialize"""

        return {}

    def get(self, session: Optional[Dict[str, Any]] = None) -> Dict:
        """Manage mapping and return shared map"""

        # Example of the plugin using the download strategy to fetch the data
        download_strategy = create_download_strategy(self.resource_config)
        read_output = download_strategy.read({})
        print(read_output)

        return {}
