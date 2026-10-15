import { useState } from "react";
import {
  ArrowDownRight,
  ArrowUpRight,
  Check,
  ChevronRight,
  Circle,
  Command,
  Crosshair,
  Eye,
  Globe2,
  Layers3,
  Menu,
  MoveUpRight,
  Play,
  Radio,
  ScanLine,
  ShieldCheck,
  Sparkles,
  X,
  Zap,
} from "lucide-react";

const heroImage = "/manus-storage/ak-robotics-hero_033b2b3c.png";
const systemImage = "/manus-storage/ak-robotics-system_42069734.png";

const layers = [
  {
    number: "01",
    title: "Hardware",
    label: "Physical intelligence",
    copy: "Autonomous mobile robots, robotic arms, sensor arrays, and safety modules designed to move with the operation.",
    tags: ["AMRs", "Robotic arms", "Sensors"],
  },
  {
    number: "02",
    title: "Software",
    label: "Orchestration layer",
    copy: "Navigation, task orchestration, fleet management, and anomaly detection in one measurable control plane.",
    tags: ["Fleet OS", "Decisioning", "Anomaly AI"],
  },
  {
    number: "03",
    title: "Human interface",
    label: "Clarity by default",
    copy: "Minimal interfaces with clear states, operator override, and logs that make every decision reviewable.",
    tags: ["Operator UI", "Overrides", "Logs"],
  },
  {
    number: "04",
    title: "Deployment pipeline",
    label: "Repeatable scale",
    copy: "Site survey to simulation, installation, calibration, and monitoring — a process built to travel across borders.",
    tags: ["Simulation", "Calibration", "Support"],
  },
];

const regions = [
  { phase: "01", place: "Bulgaria", city: "Sofia", body: "Pilot deployments, local operators, logistics partnerships.", state: "Live planning" },
  { phase: "02", place: "Balkans", city: "RO · GR · RS", body: "Cross-border automation with regional support hubs.", state: "Next horizon" },
  { phase: "03", place: "European Union", city: "DE · NL · PL", body: "Enterprise multi-site deployments and EU compliance.", state: "Scale layer" },
  { phase: "04", place: "Global", city: "DXB · YYZ · SIN", body: "A distributed operating system for modern logistics.", state: "Long view" },
];

const launchModules = [
  { icon: Command, title: "Task orchestration", detail: "Route work across agents, people, and machines." },
  { icon: Eye, title: "Decision logs", detail: "Review what happened, why it happened, and what changes next." },
  { icon: Layers3, title: "Multi-agent workflows", detail: "Compose narrow intelligence into dependable operating systems." },
  { icon: Zap, title: "Robotics integration", detail: "The physical layer arrives when the control plane is ready." },
];

export default function Home() {
  const [menuOpen, setMenuOpen] = useState(false);
  const [activeLayer, setActiveLayer] = useState(1);

  const scrollTo = (id: string) => {
    setMenuOpen(false);
    document.getElementById(id)?.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <main className="site-shell">
      <div className="grain" aria-hidden="true" />
      <nav className="top-nav" aria-label="Primary navigation">
        <button className="brand-lockup" onClick={() => scrollTo("top")} aria-label="Back to top">
          <span className="brand-mark"><Crosshair size={16} strokeWidth={1.6} /></span>
          <span className="brand-wordmark">A.K. <em>/</em> PRECISION</span>
        </button>
        <div className={`nav-links ${menuOpen ? "is-open" : ""}`}>
          <button onClick={() => scrollTo("systems")}>Systems</button>
          <button onClick={() => scrollTo("blueprint")}>Blueprint</button>
          <button onClick={() => scrollTo("expansion")}>Expansion</button>
          <button onClick={() => scrollTo("founder")}>Founder</button>
          <button className="nav-cta" onClick={() => scrollTo("contact")}>Early access <ArrowUpRight size={14} /></button>
        </div>
        <button className="menu-toggle" aria-label={menuOpen ? "Close menu" : "Open menu"} onClick={() => setMenuOpen((open) => !open)}>
          {menuOpen ? <X size={19} /> : <Menu size={19} />}
        </button>
      </nav>

      <section id="top" className="hero-section">
        <div className="hero-image" style={{ backgroundImage: `url(${heroImage})` }} aria-hidden="true" />
        <div className="hero-vignette" aria-hidden="true" />
        <div className="hero-grid" aria-hidden="true" />
        <div className="hero-content">
          <div className="eyebrow reveal"><span className="status-dot" /> FOUNDER-LED AUTOMATION / 2026</div>
          <h1 className="hero-title reveal reveal-delay-1">Precision<br /><span>at scale.</span></h1>
          <p className="hero-copy reveal reveal-delay-2">Robotics and AI systems designed for clarity, reliability, and measurable outcomes — humanly reviewable by design.</p>
          <div className="hero-actions reveal reveal-delay-3">
            <button className="button button-primary" onClick={() => scrollTo("blueprint")}>Explore the blueprint <ArrowDownRight size={16} /></button>
            <button className="button button-ghost" onClick={() => scrollTo("founder")}><span className="play-icon"><Play size={11} fill="currentColor" /></span> Meet the founder</button>
          </div>
        </div>
        <div className="hero-telemetry reveal reveal-delay-2">
          <div className="telemetry-top"><span>FIELD NODE / 001</span><span className="live-label"><Radio size={12} /> LIVE</span></div>
          <div className="telemetry-main"><span>Operator clarity</span><strong>98.4<span>%</span></strong></div>
          <div className="telemetry-line"><span /><span /><span /><span /><span /><span /><span /><span /><span /></div>
          <div className="telemetry-bottom"><span>Reviewable states</span><span>↑ 12.8%</span></div>
        </div>
        <div className="hero-index">01 <span>/</span> 06</div>
        <div className="scroll-cue"><span>Scroll to inspect</span><ArrowDownRight size={14} /></div>
      </section>

      <section className="manifesto-section section-pad">
        <div className="section-kicker"><span>00 / POSITIONING</span><span>Precision architecture for the physical world</span></div>
        <div className="manifesto-grid">
          <p className="display-quote">Automation<br /><em>without chaos.</em></p>
          <div className="manifesto-body">
            <p className="lead-copy">A.K. builds robotics and AI systems that remove noise, increase reliability, and deliver measurable automation across regions.</p>
            <div className="principle-list">
              <div><span>01</span><strong>Precision over noise</strong><p>Every system must be clear, measurable, and predictable.</p></div>
              <div><span>02</span><strong>Minimalism as power</strong><p>Interfaces should make complexity feel obvious.</p></div>
              <div><span>03</span><strong>Scalability by design</strong><p>Build once. Deploy with clarity across borders.</p></div>
            </div>
          </div>
        </div>
      </section>

      <section id="systems" className="systems-section section-pad dark-section">
        <div className="section-kicker light-kicker"><span>01 / SYSTEM LAYERS</span><span>One control plane. Four coordinated layers.</span></div>
        <div className="systems-intro">
          <div><h2>Built as a<br /><em>complete system.</em></h2></div>
          <p>Hardware is only the visible edge. The advantage lives in the operating layer that keeps every task, exception, and human decision legible.</p>
        </div>
        <div className="systems-layout">
          <div className="layer-list">
            {layers.map((layer, index) => (
              <button key={layer.number} className={`layer-row ${activeLayer === index ? "active" : ""}`} onClick={() => setActiveLayer(index)}>
                <span className="layer-number">{layer.number}</span>
                <span className="layer-title">{layer.title}</span>
                <span className="layer-arrow"><ChevronRight size={15} /></span>
              </button>
            ))}
          </div>
          <div className="layer-detail">
            <div className="detail-image" style={{ backgroundImage: `url(${systemImage})` }}>
              <div className="detail-overlay"><ScanLine size={18} /><span>Layer {layers[activeLayer].number} / active view</span></div>
            </div>
            <div className="detail-copy"><span className="mini-label">{layers[activeLayer].label}</span><p>{layers[activeLayer].copy}</p><div className="tag-list">{layers[activeLayer].tags.map((tag) => <span key={tag}>{tag}</span>)}</div></div>
          </div>
        </div>
        <div className="metrics-strip">
          <div><span>01</span><strong>Uptime</strong><em>Measured in the field</em></div>
          <div><span>02</span><strong>Tasks completed</strong><em>Visible at every site</em></div>
          <div><span>03</span><strong>Incidents</strong><em>Reviewable by default</em></div>
          <div className="metrics-mark"><ShieldCheck size={21} /><span>HUMANLY<br />REVIEWABLE</span></div>
        </div>
      </section>

      <section id="blueprint" className="blueprint-section section-pad">
        <div className="section-kicker"><span>02 / VENTURE BLUEPRINT</span><span>Robotics-as-a-Service / RaaS</span></div>
        <div className="blueprint-header"><h2>A business model<br />with <em>operational proof.</em></h2><p>Subscription-led automation for warehouses, retail, and micro-fulfillment — with deployment, support, insight, and integration built around the core.</p></div>
        <div className="revenue-grid">
          <div className="revenue-card revenue-card-feature"><div className="card-top"><span>CORE MODEL</span><span>01</span></div><h3>RaaS</h3><p>Monthly subscription + deployment fee. Capital-light for the operator. Recurring for the system.</p><div className="card-line"><span>Recurring revenue</span><b>↗</b></div></div>
          <div className="revenue-card"><div className="card-top"><span>REVENUE STREAMS</span><span>05</span></div><div className="stream-list"><div><span>01</span><strong>Monthly RaaS subscription</strong></div><div><span>02</span><strong>Deployment fee</strong></div><div><span>03</span><strong>Maintenance + support</strong></div><div><span>04</span><strong>Data insights package</strong></div><div><span>05</span><strong>Enterprise integrations</strong></div></div></div>
          <div className="revenue-card revenue-card-dark"><div className="card-top"><span>OPERATOR DASHBOARD</span><span className="live-label"><Circle size={8} fill="currentColor" /> LIVE</span></div><div className="dashboard-stats"><div><span>UPTIME</span><strong>99.97<small>%</small></strong></div><div><span>ACTIVE SITES</span><strong>04</strong></div><div><span>OPEN INCIDENTS</span><strong>00</strong></div></div><div className="spark-bars">{[42, 54, 48, 72, 64, 82, 75, 95, 88, 100].map((height, i) => <i key={i} style={{ height: `${height}%` }} />)}</div></div>
        </div>
      </section>

      <section id="expansion" className="expansion-section section-pad dark-section">
        <div className="section-kicker light-kicker"><span>03 / EXPANSION PLAN</span><span>Bulgaria → Balkans → EU → global</span></div>
        <div className="expansion-heading"><h2>Designed to<br /><em>travel.</em></h2><div className="expansion-note"><Globe2 size={18} /><p>Every layer is built for deployment across regions without losing the clarity that makes the system trustworthy.</p></div></div>
        <div className="region-timeline">
          <div className="timeline-line" />
          {regions.map((region) => <div className="region-card" key={region.phase}><div className="region-top"><span>{region.phase}</span><span className="region-state">{region.state}</span></div><h3>{region.place}</h3><strong>{region.city}</strong><p>{region.body}</p><ArrowUpRight size={17} className="region-arrow" /></div>)}
        </div>
      </section>

      <section id="founder" className="founder-section section-pad">
        <div className="section-kicker"><span>04 / FOUNDER IDENTITY</span><span>Founder & CEO / A.K.</span></div>
        <div className="founder-layout">
          <div className="founder-monogram"><span>AK</span><div className="monogram-orbit orbit-one" /><div className="monogram-orbit orbit-two" /><div className="monogram-caption">PRECISION<br />ARCHITECT</div></div>
          <div className="founder-copy"><div className="eyebrow dark-eyebrow"><span className="status-dot" /> THE FOUNDER STATEMENT</div><blockquote>“I build systems that people can trust — not because they are complex, but because they are transparent, structured, and predictable.”</blockquote><p>A.K. works at the intersection of robotics, AI orchestration, premium design, and multi-regional expansion. The ambition is not to add more technology to the world. It is to remove friction from the systems already moving it.</p><button className="text-link" onClick={() => scrollTo("contact")}>Connect with A.K. <ArrowUpRight size={15} /></button></div>
        </div>
      </section>

      <section className="launch-section section-pad dark-section">
        <div className="section-kicker light-kicker"><span>05 / MINDREPLY</span><span>The software layer starts here</span></div>
        <div className="launch-heading"><h2>Before the robots,<br /><em>the reply.</em></h2><p>MindReply is the AI-driven automation system for decisions that need to move with the operation — and remain reviewable afterward.</p></div>
        <div className="launch-grid">{launchModules.map((module, index) => { const Icon = module.icon; return <div className="launch-card" key={module.title}><div className="launch-card-top"><span>0{index + 1}</span><Icon size={18} /></div><h3>{module.title}</h3><p>{module.detail}</p><ArrowUpRight size={16} className="launch-card-arrow" /></div>; })}</div>
        <div className="launch-footer"><span><Sparkles size={15} /> Early access program</span><span>Founder-led / invite only</span><button className="button button-primary light-button" onClick={() => scrollTo("contact")}>Request access <ArrowUpRight size={15} /></button></div>
      </section>

      <section id="contact" className="contact-section section-pad">
        <div className="contact-inner"><div className="contact-label"><span className="status-dot" /> NEXT MOVE</div><h2>Build systems<br /><em>that scale.</em></h2><p>For operators, partners, and early believers building the next layer of physical work.</p><button className="button button-primary" onClick={() => window.location.href = "mailto:hello@ak-precision.io?subject=MindReply%20early%20access"}>Start a conversation <ArrowUpRight size={16} /></button></div>
      </section>

      <footer className="site-footer"><div className="footer-brand"><span className="brand-mark"><Crosshair size={15} /></span><span>A.K. / PRECISION</span></div><div className="footer-meta"><span>Robotics · AI · Automation</span><span>© 2026 A.K.</span></div><button onClick={() => scrollTo("top")} className="back-top">Back to top <ArrowUpRight size={14} /></button></footer>
    </main>
  );
}
