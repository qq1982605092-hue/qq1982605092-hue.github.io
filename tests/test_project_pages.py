from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
PROJECTS = {
    "agent_memory": ROOT / "projects/agent-memory.md",
    "calling_agent": ROOT / "projects/calling-agent.md",
    "reranker": ROOT / "projects/qwen3-reranker.md",
}


class ProjectPageContract(unittest.TestCase):
    def read_project(self, name):
        path = PROJECTS[name]
        self.assertTrue(path.is_file(), f"missing project page: {path}")
        return path.read_text(encoding="utf-8")

    def test_exact_project_routes_exist(self):
        self.assertEqual(
            {path.as_posix().split("/")[-1] for path in PROJECTS.values()},
            {"agent-memory.md", "calling-agent.md", "qwen3-reranker.md"},
        )
        for path in PROJECTS.values():
            self.assertTrue(path.is_file(), f"missing project page: {path}")

        expected_permalinks = {
            "agent_memory": 'permalink: "/projects/agent-memory/"',
            "calling_agent": 'permalink: "/projects/calling-agent/"',
            "reranker": 'permalink: "/projects/qwen3-reranker/"',
        }
        for name, permalink in expected_permalinks.items():
            self.assertIn(permalink, self.read_project(name))

    def test_shared_layout_contract(self):
        layout = ROOT / "_layouts/project.html"
        self.assertTrue(layout.is_file(), "_layouts/project.html must exist")
        source = layout.read_text(encoding="utf-8")
        for token in (
            "page.kicker",
            "page.question",
            "page.answer",
            "Back to selected work",
            "{{ content }}",
        ):
            self.assertIn(token, source)

        scss = (ROOT / "_sass/_site.scss").read_text(encoding="utf-8")
        for selector in (
            ".project-page",
            ".project-hero",
            ".project-facts",
            ".project-narrative",
            ".system-diagram",
            ".evidence-grid",
            ".project-boundary",
            ".project-next",
        ):
            self.assertIn(selector, scss)

    def test_all_pages_share_story_sections_and_safe_front_matter(self):
        for name in PROJECTS:
            source = self.read_project(name)
            self.assertIn("layout: project", source)
            for phrase in (
                "The question",
                "What I built",
                "Evidence",
                "What this does not prove",
            ):
                self.assertIn(phrase, source)
            self.assertNotRegex(source, r"/Users/|https?://code\.nuanwainfo")

    def test_agent_memory_evidence(self):
        source = self.read_project("agent_memory")
        for phrase in (
            "EvoWalker",
            "1,321 / 1,540",
            "85.78%",
            "LoCoMo official LLM-as-a-Judge",
            "75.89%",
            "80.69%",
            "71.88%",
            "92.63%",
            "matched ablations are not yet complete",
            "raw-only LongMemEval result is not reported as an EvoWalker result",
            "Embodied-agent connection",
        ):
            self.assertIn(phrase, source)
        for forbidden in ("94.61%", "89.10%", "SOTA", "state-of-the-art"):
            self.assertNotIn(forbidden, source)

    def test_calling_agent_evidence(self):
        source = self.read_project("calling_agent")
        for phrase in (
            "Memory",
            "Prediction Cache",
            "Rerank",
            "FastComposer",
            "Router",
            "Generator",
            "Verifier",
            "Predictor",
            "offline replay",
            "Fast path",
            "Fallback path",
        ):
            self.assertIn(phrase, source)
        for forbidden in (
            "SFT",
            "DPO",
            "LoRA",
            "GRPO",
            "finite-state machine",
            "conversion lift",
            "accuracy improvement",
            "latency improvement",
            "guarantees compliance",
        ):
            self.assertNotIn(forbidden, source)

    def test_reranker_evidence(self):
        source = self.read_project("reranker")
        for phrase in (
            "Qwen3-Reranker-0.6B",
            "LoRA SFT",
            "pointwise yes/no",
            "1 positive + 3 negatives",
            "Current data assets",
            "15,704",
            "1,749",
            "Archived evaluation",
            "checkpoint-135",
            "85.39%",
            "93.12%",
            "earlier validation split",
            "not a current-data evaluation",
        ):
            self.assertIn(phrase, source)
        self.assertNotIn("full-corpus retriever", source)

    def test_homepage_has_three_detail_links_only(self):
        data = (ROOT / "_data/projects.yml").read_text(encoding="utf-8")
        self.assertEqual(len(re.findall(r"^  url:", data, re.MULTILINE)), 3)
        for route in (
            "/projects/agent-memory/",
            "/projects/calling-agent/",
            "/projects/qwen3-reranker/",
        ):
            self.assertIn(route, data)

        component = (ROOT / "_includes/project-entry.html").read_text(
            encoding="utf-8"
        )
        self.assertIn("include.project.url", component)
        self.assertIn("relative_url", component)
        self.assertIn("Read project", component)

    def test_calling_agent_homepage_copy_matches_evidence(self):
        data = (ROOT / "_data/projects.yml").read_text(encoding="utf-8")
        calling = data.split("- id: calling-agent", 1)[1].split(
            "- id: qwen3-reranker", 1
        )[0]
        self.assertIn('title: "Strategy-Driven AI Calling Agent"', calling)
        self.assertIn("Memory, strategy routing, constrained generation", calling)
        self.assertIn("predictive fast path", calling)
        for phrase in (
            "State-Driven",
            "transition conditions",
            "model post-training",
        ):
            self.assertNotIn(phrase, calling)


if __name__ == "__main__":
    unittest.main()
