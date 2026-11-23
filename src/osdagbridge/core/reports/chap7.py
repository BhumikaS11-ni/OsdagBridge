def ch7_quantities(input_dict, assets_dir=None):
    report_tex = r"""
\chapter{Material Take-off \& Quantity Summary}
\label{ch:material-takeoff}

\noindent\textbf{Table 7.1  Bill of Materials (Steel, Concrete, and Reinforcement Quantities)}

\begingroup
\setlength{\tabcolsep}{3.5pt}
\begin{longtable}{|C{1.0cm}|L{3.8cm}|C{2.6cm}|C{1.8cm}|C{1.8cm}|C{1.8cm}|C{1.8cm}|}
\hline
\textbf{S.N.} & \textbf{Item Description} & \textbf{Volume} & \textbf{Quantity} & \textbf{Total Volume} & \textbf{Weight (MT)} & \textbf{Total Weight (MT)} \\
\hline
1 & Structural Steel (IS 2062) for Girders & """ + str(input_dict.get("steel_girders_vol_formula", "N.A.")) + r""" & """ + str(input_dict.get("steel_girders_qty", "N.A.")) + r""" & """ + str(input_dict.get("steel_girders_vol_total", "N.A.")) + r""" & """ + str(input_dict.get("steel_girders_wt_single", "N.A.")) + r""" & """ + str(input_dict.get("steel_girders_wt_total", "N.A.")) + r""" \\
\hline
2(a) & Cross Bracing - Top Chord & """ + str(input_dict.get("bracing_top_vol_formula", "N.A.")) + r""" & """ + str(input_dict.get("bracing_top_qty", "N.A.")) + r""" & """ + str(input_dict.get("bracing_top_vol_total", "N.A.")) + r""" & """ + str(input_dict.get("bracing_top_wt_single", "N.A.")) + r""" & """ + str(input_dict.get("bracing_top_wt_total", "N.A.")) + r""" \\
\hline
2(b) & Cross Bracing - Bottom Chord & """ + str(input_dict.get("bracing_bot_vol_formula", "N.A.")) + r""" & """ + str(input_dict.get("bracing_bot_qty", "N.A.")) + r""" & """ + str(input_dict.get("bracing_bot_vol_total", "N.A.")) + r""" & """ + str(input_dict.get("bracing_bot_wt_single", "N.A.")) + r""" & """ + str(input_dict.get("bracing_bot_wt_total", "N.A.")) + r""" \\
\hline
2(c) & Cross Bracing - Diagonal Chord & """ + str(input_dict.get("bracing_diag_vol_formula", "N.A.")) + r""" & """ + str(input_dict.get("bracing_diag_qty", "N.A.")) + r""" & """ + str(input_dict.get("bracing_diag_vol_total", "N.A.")) + r""" & """ + str(input_dict.get("bracing_diag_wt_single", "N.A.")) + r""" & """ + str(input_dict.get("bracing_diag_wt_total", "N.A.")) + r""" \\
\hline
3 & Concrete (M40) for Deck Slab & """ + str(input_dict.get("concrete_deck_vol_formula", "N.A.")) + r""" & """ + str(input_dict.get("concrete_deck_qty", "N.A.")) + r""" & """ + str(input_dict.get("concrete_deck_vol_total", "N.A.")) + r""" & """ + str(input_dict.get("concrete_deck_wt_single", "N.A.")) + r""" & """ + str(input_dict.get("concrete_deck_wt_total", "N.A.")) + r""" \\
\hline
4 & Reinforcement Steel (Fe 500) & """ + str(input_dict.get("rebar_deck_vol_formula", "N.A.")) + r""" & """ + str(input_dict.get("rebar_deck_qty", "N.A.")) + r""" & """ + str(input_dict.get("rebar_deck_vol_total", "N.A.")) + r""" & """ + str(input_dict.get("rebar_deck_wt_single", "N.A.")) + r""" & """ + str(input_dict.get("rebar_deck_wt_total", "N.A.")) + r""" \\
\hline
5 & Shear Stud Connectors & """ + str(input_dict.get("shear_studs_vol_formula", "N.A.")) + r""" & """ + str(input_dict.get("shear_studs_qty", "N.A.")) + r""" & """ + str(input_dict.get("shear_studs_vol_total", "N.A.")) + r""" & """ + str(input_dict.get("shear_studs_wt_single", "N.A.")) + r""" & """ + str(input_dict.get("shear_studs_wt_total", "N.A.")) + r""" \\
\hline
6 & Crash Barrier & """ + str(input_dict.get("crash_barrier_vol_formula", "N.A.")) + r""" & """ + str(input_dict.get("crash_barrier_qty", "N.A.")) + r""" & """ + str(input_dict.get("crash_barrier_vol_total", "N.A.")) + r""" & """ + str(input_dict.get("crash_barrier_wt_single", "N.A.")) + r""" & """ + str(input_dict.get("crash_barrier_wt_total", "N.A.")) + r""" \\
\hline
\end{longtable}
"""

    chart_tex = ""

    if assets_dir:
        try:
            import os
            import matplotlib.pyplot as plt

            def numeric_value(key):
                try:
                    value = float(input_dict.get(key))
                    return value if value >= 0 else None
                except (TypeError, ValueError):
                    return None

            # Steel quantities in metric tonnes
            steel_items = [
                ("Girders", "steel_girders_wt_total"),
                ("Top Bracing", "bracing_top_wt_total"),
                ("Bottom Bracing", "bracing_bot_wt_total"),
                ("Diagonal Bracing", "bracing_diag_wt_total"),
            ]

            steel_labels = []
            steel_values = []

            for label, key in steel_items:
                value = numeric_value(key)
                if value is not None:
                    steel_labels.append(label)
                    steel_values.append(value)

            # Concrete volume and reinforcement weight
            concrete_volume = numeric_value("concrete_deck_vol_total")
            rebar_weight = numeric_value("rebar_deck_wt_total")

            os.makedirs(assets_dir, exist_ok=True)

            if steel_values:
                fig, ax = plt.subplots(figsize=(8, 4))
                ax.bar(steel_labels, steel_values)
                ax.set_ylabel("Weight (MT)")
                ax.set_title("Structural Steel Quantity")
                ax.grid(axis="y", alpha=0.25)
                plt.xticks(rotation=15, ha="right")
                fig.tight_layout()

                steel_path = os.path.join(
                    assets_dir, "steel_quantity_chart.png"
                )
                fig.savefig(steel_path, dpi=180, bbox_inches="tight")
                plt.close(fig)

                chart_tex += (
                    r"\begin{figure}[H]" + "\n"
                    r"\centering" + "\n"
                    r"\includegraphics[width=0.85\textwidth]{"
                    + _tex(steel_path) + "}\n"
                    r"\caption{Structural Steel Quantity}" + "\n"
                    r"\end{figure}" + "\n"
                )

            if concrete_volume is not None and rebar_weight is not None:
                # Separate axes because the units differ
                fig, ax1 = plt.subplots(figsize=(8, 4))
                ax2 = ax1.twinx()

                ax1.bar(
                    ["Concrete"],
                    [concrete_volume],
                    label="Concrete Volume (m³)",
                    alpha=0.7,
                )
                ax2.bar(
                    ["Reinforcement"],
                    [rebar_weight],
                    label="Reinforcement Weight (MT)",
                    alpha=0.7,
                )

                ax1.set_ylabel("Concrete Volume (m³)")
                ax2.set_ylabel("Reinforcement Weight (MT)")
                ax1.set_title("Concrete and Reinforcement Quantities")
                fig.tight_layout()

                material_path = os.path.join(
                    assets_dir, "concrete_reinforcement_chart.png"
                )
                fig.savefig(material_path, dpi=180, bbox_inches="tight")
                plt.close(fig)

                chart_tex += (
                    r"\begin{figure}[H]" + "\n"
                    r"\centering" + "\n"
                    r"\includegraphics[width=0.85\textwidth]{"
                    + _tex(material_path) + "}\n"
                    r"\caption{Concrete and Reinforcement Quantities}" + "\n"
                    r"\end{figure}" + "\n"
                )

        except Exception:
            import logging
            logging.getLogger(__name__).exception(
                "Could not generate material quantity charts"
            )

    return report_tex + "\n" + chart_tex
