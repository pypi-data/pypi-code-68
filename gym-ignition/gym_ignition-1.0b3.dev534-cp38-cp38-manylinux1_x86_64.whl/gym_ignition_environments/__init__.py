# Copyright (C) 2020 Istituto Italiano di Tecnologia (IIT). All rights reserved.
# This software may be modified and distributed under the terms of the
# GNU Lesser General Public License v2.1 or any later version.

import numpy
from .tasks import pendulum_swingup
from gym.envs.registration import register
from .tasks import cartpole_discrete_balancing
from .tasks import cartpole_continuous_swingup
from .tasks import cartpole_continuous_balancing

max_float = float(numpy.finfo(numpy.float32).max)

register(
    id='Pendulum-Gazebo-v0',
    entry_point='gym_ignition.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=5000,
    kwargs={'task_cls': pendulum_swingup.PendulumSwingUp,
            'agent_rate': 1000,
            'physics_rate': 1000,
            'real_time_factor': max_float,
            })

register(
    id='CartPoleDiscreteBalancing-Gazebo-v0',
    entry_point='gym_ignition.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=5000,
    kwargs={'task_cls': cartpole_discrete_balancing.CartPoleDiscreteBalancing,
            'agent_rate': 1000,
            'physics_rate': 1000,
            'real_time_factor': max_float,
            })

register(
    id='CartPoleContinuousBalancing-Gazebo-v0',
    entry_point='gym_ignition.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=5000,
    kwargs={'task_cls': cartpole_continuous_balancing.CartPoleContinuousBalancing,
            'agent_rate': 1000,
            'physics_rate': 1000,
            'real_time_factor': max_float,
            })

register(
    id='CartPoleContinuousSwingup-Gazebo-v0',
    entry_point='gym_ignition.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=5000,
    kwargs={'task_cls': cartpole_continuous_swingup.CartPoleContinuousSwingup,
            'agent_rate': 1000,
            'physics_rate': 1000,
            'real_time_factor': max_float,
            })
