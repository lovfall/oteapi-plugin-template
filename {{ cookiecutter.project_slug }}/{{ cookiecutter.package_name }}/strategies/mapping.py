# pylint: disable=W0511, W0613
"""
Demo mapping strategy class
"""
from dataclasses import dataclass
from typing import Any, Dict, Optional

from oteapi.models.mappingconfig import MappingConfig
from oteapi.plugins.factories import StrategyFactory


@dataclass
@StrategyFactory.register(("mappingType", "mapping/DEMO"))
class DemoMappingStrategy:
    """Mapping Interface"""

    mapping_config: MappingConfig

    def initialize(self, session: Optional[Dict[str, Any]] = None) -> Dict:
        """Initialize mapping"""

        # TODO: Add initializing logic

        return {}

    def get(self, session: Optional[Dict[str, Any]] = None) -> Dict:
        """Manage mapping and return shared map"""

        # TODO: Add mapping logic

        return {}