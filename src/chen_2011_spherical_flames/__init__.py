"""chen-2011-spherical-flames-gaia

Formalization of Chen (2011) "On the extraction of laminar flame speed and
Markstein length from outwardly propagating spherical flames" (Combustion and
Flame 158, 291-300) together with the independent reproduction trace
chen-2011-cnf-158.
"""

from .motivation import *  # noqa: F401,F403
from .s1_extraction_models import *  # noqa: F401,F403
from .s2_nq_window import *  # noqa: F401,F403
from .s3_cantera_validation import *  # noqa: F401,F403
from .s4_asurf_reproduction import *  # noqa: F401,F403
from .s5_taylor_reanalysis import *  # noqa: F401,F403
from .s6_qg_audit import *  # noqa: F401,F403

__all__ = [
    "chen2011_reproducible",
    "reproduction_13_of_14",
    "reproduction_lessons",
    "cantera_validates_paper_sl",
    "taylor_reanalysis_agreement",
    "nq_window_requirement",
    "error_ordering_le_ne_1",
    "error_zero_at_le1",
    "error_def_residual_eq6",
]
