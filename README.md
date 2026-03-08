<p align="center" style="margin-bottom: 0.5em;">
  <a href="https://github.com/LINK" style="display:inline-block; padding:8px 16px; margin:4px; background-color:#1f6feb; color:white; text-decoration:none; border-radius:6px; font-size:14px;">GitHub</a>
  <a href="https://NEUREPS_LINK" style="display:inline-block; padding:8px 16px; margin:4px; background-color:#1f6feb; color:white; text-decoration:none; border-radius:6px; font-size:14px;">NeurReps '25 Paper</a>
  <a href="https://COSYNE_LINK" style="display:inline-block; padding:8px 16px; margin:4px; background-color:#1f6feb; color:white; text-decoration:none; border-radius:6px; font-size:14px;">COSYNE '26 Poster</a>
</p>

# From Black Boxes to Circuit Diagrams
### Time-Resolved Neuronal Circuit Discovery in RNNs via Windowed Causal Interventions and Local Linearization

![Time-resolved neuronal circuit discovery pipeline for RNNs.](/images/Time-Resolved-Circuit-Discovery-in-RNNs-Summary-Figure.png)
<div style="text-align: justify;">
  <em>Time-resolved neuronal circuit discovery pipeline for RNNs.</em> Given a trained RNN, our method proceeds in two stages. 
    Windowed causal interventions (Stage 1) identifies task-critical neurons by intervening on hidden state activations within temporal windows $W = (t_s, t_e)$.
    Ablation tests necessity while activation patching tests sufficiency.
    This yields a ranked set of causally-important neurons for each computational epoch.
    Local linearization (Stage 2) characterizes how all neurons interact by computing the instantaneous effective connectivity $S_{j \to i}(t)$, which decomposes influence into postsynaptic gain (gate $g_i(t)$), synaptic weight (wire $W_{ij}$), and presynaptic activity (signal $h_{t-1}[j]$).
    This projects the recurrent dynamics onto the local tangent space at each timestep. 
    Combining the two stages, the time-resolved circuit diagrams reveal how subcircuit configurations dynamically reconfigure across a computation.
</div>

### Abstract
Recurrent neural networks (RNNs) are a prominent modelling tool in computational neuroscience. Yet, their black box nature limits their utility for revealing explicit structure-function relationships in neural circuits. In this work, we present a circuit discovery framework that adapts causal intervention techniques from mechanistic interpretability to the recurrent, multi-step computation in RNNs. By combining windowed ablations with Jacobian-based linearization of the hidden state trajectories, we estimate effective connectivity across the RNN as it evolves, thereby revealing how task-relevant computations are implemented through dynamically coordinated subcircuits. Across synthetic tasks with known mechanisms, our pipeline recovers operative circuits with high precision while demonstrating robustness advantages over correlation-based selection methods. On applying our methods to anatomically-constrained RNNs trained on a subset of the Allen Institute's Visual Behavior dataset, we validate the role of VIP interneurons in processing unexpected stimuli while revealing temporal patterns in their causal contributions that are invisible to static analyses. Our experiments further suggest that intrinsic VIP timing drives prediction error formation in the network, consequently bridging the timing-code and predictive-processing interpretations of VIP function.
