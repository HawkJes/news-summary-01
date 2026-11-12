# news-summary-01: a deterministic, offline entry. It writes the embedded
# summary of Wednesday 11 November 2026 to $MAKEFUN_OUTPUT_DIR/entry.txt
# (default /output). Standard library only, no network, no randomness:
# every run writes byte-identical output.
import os

SUMMARY = """World news, Wednesday 11 November 2026: Three Iranian-backed operatives were charged over nearly 20 U.S. and European plots, including one at RAF Fairford; Secretary Bessent moved to a military base after threats (NYT, Fox News). A Saudi tanker, NCC FAJR, faced a possible attack in the Strait of Hormuz, all crew safe, as Iran claimed two supertankers hit mines, unverified (UKMTO, ANI). Trump called the war with Iran militarily 'effectively over'; Rubio said U.S. pressure had made major combat unnecessary but warned of strikes if Iran crossed red lines (AP, NYT). Ukraine-Russia-U.S. talks in Abu Dhabi ended with no peace deal, but a 1,000-1,500-a-side prisoner swap was agreed. NATO jets scrambled as at least four drones strayed into Baltic airspace during Ukrainian strikes on Russia, which also set a Baltic port ablaze (the Independent). Israeli forces killed at least seven in Gaza, including a father and his 13-year-old son, health officials said. U.S. inflation rose 0.4% in October, beating forecasts, and Fed Governor Waller said a half-point December rise should be considered, pushing the 10-year yield above 5% (CNBC). British police arrested a 41-year-old U.S. soldier in a NATO unit in England suspected of spying for Russia. At COP31, 102 leaders and 300 ministers met as U.N. chief Guterres warned the slow response put the world on a path to destruction (BBC). Israel's parliament was sworn in after deadlock cost Netanyahu his majority, leaving rivals with no clear path to a government and Eisenkot to try to form one. China's trade surplus passed $1 trillion in ten months, customs said (NYT). House Republicans blocked impeaching Defense Secretary Hegseth and made Jim Jordan minority leader. Anthropic filed for a Nasdaq listing valuing it at up to $1.4 trillion. Delhi's air stayed poor after Diwali at 299 on the air quality index, and pupils moved to hybrid classes. Spain held its first general strike in 14 years, with mass protests and clashes in Barcelona."""


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SUMMARY)


if __name__ == "__main__":
    main()
