"""EXP-027 Blinded Evaluator & Scoring Harness.

Evaluates anonymized UUID stimuli against neutral, pre-registered prompts:
- Formats: VLT_WEBP, GRID128_WEBP, GRID512_WEBP, BASELINE_T0.
- Zero semantic leak: stimuli use neutral 12-char hex UUIDs.
- Prompt text is strictly content-neutral (no event counts or slot hints).
- Collects structured extraction + free-text narrative.
- Scores against frozen verified ground truth using exact classification metrics.
"""

import os
import json
from typing import Dict, Any, List

EVALUATION_PROMPTS = {
    "VLT_WEBP": """WISSENSCHAFTLICHER VIDEO-BLINDTEST:

Analysiere die dargestellte Szene völlig frei und neutral:
Das Bild ist ein 128x128 E3-K12 Visual Carrier (4 Quadranten à 64x64):
- Oben-Links: Basiszustand (Frame t=0)
- Oben-Rechts: Temporale Kinematik (R=P0 Mittelwert, G=P2 Krümmung, B=Walsh-Moden)
- Unten-Links: Chromatische Trägerschicht (Cb=P1 Trend, Cr=Walsh-Moden)
- Unten-Rechts: Neutralgrau (128)

AUFGABE:
Beschreibe ausschließlich, was du in der dargestellten Szene erkennen kannst, in zeitlicher Reihenfolge:
1. Welche Objekte existieren in der Szene?
2. Bewegt sich ein Objekt, und wenn ja, in welche primäre Richtung?
3. Tritt eine Verdeckung (Okklusion) durch ein Hindernis auf (keine, partiell oder vollständig)?
4. Taucht das Objekt nach einer Verdeckung wieder auf, und auf welcher Seite?
5. Tritt ein Richtungswechsel (Abprallen / Umkehren) auf?
6. Tritt ein kurzes Helligkeits- oder Farbereignis (Puls/Blitz) auf?
Kennzeichne Unsicherheiten ausdrücklich. Erfinde keine nicht sichtbaren Ereignisse.

Antworte im folgenden JSON-Format:
{
  "narrative": "Deine freie zeitliche Beschreibung...",
  "moving_object_count": 1,
  "object_shape": "sphere" | "other" | "unknown",
  "primary_motion": "left_to_right" | "right_to_left" | "approach_then_reverse" | "static",
  "occlusion_type": "none" | "partial" | "full" | "unknown",
  "reemergence_observed": true | false,
  "reemergence_side": "right" | "left" | "none",
  "reversal_observed": true | false,
  "pulse_observed": true | false,
  "confidence": 0.0
}""",

    "GRID_FORMAT": """WISSENSCHAFTLICHER VIDEO-BLINDTEST:

Analysiere die dargestellte Szene völlig frei und neutral:
Das Bild ist ein 8x8 Kontaktbogen aus 64 zeitlich aufeinanderfolgenden Videobildern.
Die Zeit verläuft zeilenweise von oben-links nach unten-rechts (Zeile 0 = Anfang, Zeile 7 = Ende).

AUFGABE:
Beschreibe ausschließlich, was du in der dargestellten Szene erkennen kannst, in zeitlicher Reihenfolge:
1. Welche Objekte existieren in der Szene?
2. Bewegt sich ein Objekt, und wenn ja, in welche primäre Richtung?
3. Tritt eine Verdeckung (Okklusion) durch ein Hindernis auf (keine, partiell oder vollständig)?
4. Taucht das Objekt nach einer Verdeckung wieder auf, und auf welcher Seite?
5. Tritt ein Richtungswechsel (Abprallen / Umkehren) auf?
6. Tritt ein kurzes Helligkeits- oder Farbereignis (Puls/Blitz) auf?
Kennzeichne Unsicherheiten ausdrücklich. Erfinde keine nicht sichtbaren Ereignisse.

Antworte im folgenden JSON-Format:
{
  "narrative": "Deine freie zeitliche Beschreibung...",
  "moving_object_count": 1,
  "object_shape": "sphere" | "other" | "unknown",
  "primary_motion": "left_to_right" | "right_to_left" | "approach_then_reverse" | "static",
  "occlusion_type": "none" | "partial" | "full" | "unknown",
  "reemergence_observed": true | false,
  "reemergence_side": "right" | "left" | "none",
  "reversal_observed": true | false,
  "pulse_observed": true | false,
  "confidence": 0.0
}"""
}


def score_evaluator_response(response: Dict[str, Any], ground_truth: Dict[str, Any]) -> Dict[str, Any]:
    """Calculate exact category matches and binary confusion metrics."""
    scores = {}
    
    # Motion direction
    expected_motion = ground_truth.get("primary_motion")
    actual_motion = response.get("primary_motion")
    scores["motion_direction_correct"] = (actual_motion == expected_motion)
    
    # Occlusion class (none, partial, full)
    expected_occ = ground_truth.get("occlusion_type")
    actual_occ = response.get("occlusion_type")
    scores["occlusion_type_correct"] = (actual_occ == expected_occ)
    
    # Reversal detection
    expected_rev = ground_truth.get("reversal_present", False)
    actual_rev = response.get("reversal_observed", False)
    scores["reversal_correct"] = (actual_rev == expected_rev)
    
    # Re-emergence detection
    expected_reemerg = ground_truth.get("reemergence_present", False)
    actual_reemerg = response.get("reemergence_observed", False)
    scores["reemergence_correct"] = (actual_reemerg == expected_reemerg)
    
    # Pulse detection
    expected_pulse = ground_truth.get("brightness_pulse_present", False)
    actual_pulse = response.get("pulse_observed", False)
    scores["pulse_correct"] = (actual_pulse == expected_pulse)
    
    # Composite score (0..5)
    total_points = sum(1 for v in scores.values() if v)
    scores["total_score"] = total_points
    scores["accuracy_pct"] = (total_points / 5.0) * 100.0
    return scores


if __name__ == "__main__":
    print("EXP-027 Evaluator & Scoring Harness ready.")
