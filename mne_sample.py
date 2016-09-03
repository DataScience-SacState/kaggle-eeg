#!/usr/bin/python

import os.path as op
import mne
import scipy
import numpy

import mne.viz

data_path = op.join(mne.datasets.sample.data_path(), 'MEG', 'sample')
raw = mne.io.read_raw_fif(op.join(data_path, 'sample_audvis_raw.fif'))
events = mne.read_events(op.join(data_path, 'sample_audvis_raw-eve.fif'))

raw.plot(block=True, events=events)
