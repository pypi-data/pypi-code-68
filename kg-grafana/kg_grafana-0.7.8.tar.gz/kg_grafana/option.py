from typing import Sequence, Mapping, Any

from kubragen.configfile import ConfigFile
from kubragen.data import Data
from kubragen.kdatahelper import KDataHelper_Volume
from kubragen.option import OptionDef, OptionDefFormat
from kubragen.options import Options


class GrafanaOptions(Options):
    """
    Options for the Grafana builder.

    .. list-table::
        :header-rows: 1

        * - option
          - description
          - allowed types
          - default value
        * - basename
          - object names prefix
          - str
          - ```grafana```
        * - namespace
          - namespace
          - str
          - ```default```
        * - config |rarr| install_plugins
          - install plugins
          - Sequence
          - ```[]```
        * - config |rarr| service_port
          - service port
          - int
          - 3000
        * - config |rarr| provisioning |rarr| datasources
          - Grafana datasource provisioning
          - str, Sequence, ConfigFile
          -
        * - config |rarr| provisioning |rarr| plugins
          - Grafana plugins provisioning
          - str, Sequence, ConfigFile
          -
        * - config |rarr| provisioning |rarr| dashboards
          - Grafana dashboards provisioning
          - str, Sequence, ConfigFile
          -
        * - container |rarr| grafana
          - grafana container image
          - str
          - ```grafana/grafana:<version>```
        * - kubernetes |rarr| volumes |rarr| data
          - Kubernetes data volume
          - Mapping, :class:`KData_Value`, :class:`KData_ConfigMap`, :class:`KData_Secret`
          - ```{'emptyDir': {}}```
        * - kubernetes |rarr| resources |rarr| deployment
          - Kubernetes Deployment resources
          - Mapping
          -
    """
    def define_options(self):
        """
        Declare the options for the Grafana builder.

        :return: The supported options
        """
        return {
            'basename': OptionDef(required=True, default_value='grafana', allowed_types=[str]),
            'namespace': OptionDef(required=True, default_value='default', allowed_types=[str]),
            'config': {
                'install_plugins': OptionDef(default_value=[], allowed_types=[Sequence]),
                'service_port': OptionDef(required=True, default_value=3000, allowed_types=[int]),
                'provisioning': {
                    'datasources': OptionDef(allowed_types=[str, Sequence, ConfigFile]),
                    'plugins': OptionDef(allowed_types=[str, Sequence, ConfigFile]),
                    'dashboards': OptionDef(allowed_types=[str, Sequence, ConfigFile]),
                },
            },
            'container': {
                'grafana': OptionDef(required=True, default_value='grafana/grafana:7.2.0', allowed_types=[str]),
            },
            'kubernetes': {
                'volumes': {
                    'data': OptionDef(required=True, format=OptionDefFormat.KDATA_VOLUME,
                                      default_value={'emptyDir': {}},
                                      allowed_types=[Mapping, *KDataHelper_Volume.allowed_kdata()]),
                },
                'resources': {
                    'deployment': OptionDef(allowed_types=[Mapping]),
                }
            },
        }


class GrafanaOptions_Default_Resources_Deployment(Data):
    """
    Default option value for:

    ```kubernetes.resources.deployment```
    """
    def is_enabled(self) -> bool:
        return True

    def get_value(self) -> Any:
        return {
            'requests': {
                'cpu': '100m',
                'memory': '128Mi'
            },
            'limits': {
                'cpu': '100m',
                'memory': '128Mi'
            },
        }
