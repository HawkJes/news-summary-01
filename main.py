# news-summary-01: a deterministic, offline entry. It writes the embedded
# summary of Wednesday 11 November 2026 to $MAKEFUN_OUTPUT_DIR/entry.txt
# (default /output). Standard library only, no network, no randomness:
# every run writes byte-identical output.
import os

SUMMARY = """World news, Wednesday 11 November 2026: U.S. prosecutors charged three Iranian-backed operatives over nearly 20 plots in the U.S. and Europe, including one at RAF Fairford in England; Treasury Secretary Scott Bessent was moved to a military base after threats (NYT, Fox News). Ukraine-Russia-U.S. talks in Abu Dhabi ended with no peace deal, though a 1,000-1,500-a-side prisoner swap was agreed in principle, and Kyiv rejected a U.S. proposal over unoccupied Donbas. At COP31 in Antalya, 102 heads of state and 300 ministers met as U.N. chief Guterres warned the slow response had put the world on a path to destruction; Russia, India and U.S. leaders were absent, the BBC reported. Israel's parliament was sworn in after a deadlocked election; Netanyahu lost his majority, but rivals have no clear path to a government, leaving Gadi Eisenkot to try to form one.
British police arrested a 41-year-old U.S. soldier in a NATO unit in England suspected of spying for Russia. President Trump said the war with Iran was militarily 'effectively over'; Secretary of State Rubio said U.S. economic pressure had made major combat unnecessary but warned Washington might still strike if Iran crossed red lines. In Gaza, Israeli forces killed at least seven people, including a father and his 13-year-old son, health officials said. China's trade surplus passed $1 trillion in the first 10 months, customs said. U.S. House Republicans blocked impeaching Defense Secretary Pete Hegseth and made Jim Jordan their minority leader after the midterm defeat. Anthropic filed for a Nasdaq listing valuing it at up to $1.4 trillion, and hot inflation lifted the odds of a December Fed rate rise to near certainty.
Delhi's air stayed poor after Diwali at 299 on the air quality index, and pupils moved to hybrid classes. Spain held its first general strike in 14 years, with mass protests and clashes in Barcelona. Chile's Atacama Desert burst into its biggest wildflower bloom in decades across 7,000 sq miles."""


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SUMMARY)


if __name__ == "__main__":
    main()
