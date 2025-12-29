"""
Advanced AI Research Trends in MENA Universities
Enhanced Multi-Agent System with Advanced Features
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import random
from datetime import datetime, timedelta
import time

# -----------------------------
# Enhanced Simulated Database
# -----------------------------
class ResearchDatabase:
    def __init__(self):
        self.universities = [
            {"name": "KAUST", "country": "Saudi Arabia", "ranking": 1},
            {"name": "MBZUAI", "country": "UAE", "ranking": 2},
            {"name": "AUC", "country": "Egypt", "ranking": 3},
            {"name": "Qatar University", "country": "Qatar", "ranking": 4},
            {"name": "UAE University", "country": "UAE", "ranking": 5},
            {"name": "King Saud University", "country": "Saudi Arabia", "ranking": 6},
            {"name": "Cairo University", "country": "Egypt", "ranking": 7},
            {"name": "AUB", "country": "Lebanon", "ranking": 8},
            {"name": "UAEU", "country": "UAE", "ranking": 9}
        ]
        
        self.topics = [
            {"name": "Computer Vision", "trend": "↑", "growth": 15},
            {"name": "NLP", "trend": "↑↑", "growth": 25},
            {"name": "Deep Learning", "trend": "→", "growth": 5},
            {"name": "Robotics", "trend": "↑", "growth": 12},
            {"name": "Machine Learning", "trend": "→", "growth": 3},
            {"name": "AI Ethics", "trend": "↑↑↑", "growth": 45},
            {"name": "Generative AI", "trend": "↑↑↑", "growth": 85},
            {"name": "Reinforcement Learning", "trend": "↑", "growth": 18},
            {"name": "Edge AI", "trend": "↑↑", "growth": 35},
            {"name": "Explainable AI", "trend": "↑↑", "growth": 28}
        ]
        
        # Define conferences BEFORE calling methods that use it
        self.conferences = ["NeurIPS", "CVPR", "ICML", "AAAI", "ACL", "ICLR", "KDD", "Local"]
        
        self.papers = self._generate_papers()
        self.collaborations = self._generate_collaborations()
    
    def _generate_papers(self):
        papers = []
        for i in range(500):
            uni = random.choice(self.universities)
            topic = random.choice(self.topics)
            year = random.choice([2022, 2023, 2024])
            
            # More realistic citation distribution
            base_citations = random.randint(5, 150)
            if year == 2022:
                base_citations = int(base_citations * 1.5)  # Older papers have more citations
            elif year == 2024:
                base_citations = int(base_citations * 0.7)  # Newer papers have fewer
            
            papers.append({
                "id": f"P{i+1:04d}",
                "title": f"{topic['name']} Applications in Smart Systems - Study {i+1}",
                "university": uni['name'],
                "country": uni['country'],
                "topic": topic['name'],
                "year": year,
                "month": random.randint(1, 12),
                "citations": base_citations,
                "authors": random.randint(2, 8),
                "conference": random.choice(self.conferences),
                "open_access": random.choice([True, False]),
                "h_index_contribution": random.randint(1, 5)
            })
        return pd.DataFrame(papers)
    
    def _generate_collaborations(self):
        collabs = []
        unis = [u['name'] for u in self.universities]
        for _ in range(50):
            uni1, uni2 = random.sample(unis, 2)
            collabs.append({
                "uni1": uni1,
                "uni2": uni2,
                "papers": random.randint(3, 15),
                "citations": random.randint(50, 300)
            })
        return pd.DataFrame(collabs)

# -----------------------------
# Enhanced Agents with Progress Tracking
# -----------------------------
class SearchAgent:
    def __init__(self):
        self.name = "🔍 Publication Search Agent"
        self.status = "idle"
    
    def filter_papers(self, db, universities, topics, year_range, min_citations):
        self.status = "working"
        time.sleep(0.3)  # Simulate processing
        
        df = db.papers[
            (db.papers['university'].isin(universities)) &
            (db.papers['topic'].isin(topics)) &
            (db.papers['year'] >= year_range[0]) &
            (db.papers['year'] <= year_range[1]) &
            (db.papers['citations'] >= min_citations)
        ]
        
        self.status = "completed"
        return df, {
            "papers_found": len(df),
            "total_citations": df['citations'].sum(),
            "avg_citations": df['citations'].mean() if not df.empty else 0
        }

class AnalysisAgent:
    def __init__(self):
        self.name = "📊 Topic Modeling Agent"
        self.status = "idle"
    
    def compute_advanced_stats(self, papers):
        self.status = "working"
        time.sleep(0.4)
        
        # University Statistics
        uni_stats = papers.groupby('university').agg({
            'citations': ['sum', 'mean', 'count'],
            'h_index_contribution': 'sum'
        }).round(2)
        uni_stats.columns = ['total_citations', 'avg_citations', 'paper_count', 'h_index']
        uni_stats = uni_stats.sort_values('total_citations', ascending=False)
        
        # Topic Statistics
        topic_stats = papers.groupby('topic').agg({
            'citations': ['sum', 'mean', 'count']
        }).round(2)
        topic_stats.columns = ['total_citations', 'avg_citations', 'paper_count']
        topic_stats = topic_stats.sort_values('total_citations', ascending=False)
        
        # Yearly Trends
        yearly_trends = papers.groupby(['year', 'topic']).size().reset_index(name='count')
        
        # Country Statistics
        country_stats = papers.groupby('country').agg({
            'citations': 'sum',
            'id': 'count'
        }).round(2)
        country_stats.columns = ['total_citations', 'paper_count']
        
        self.status = "completed"
        return uni_stats, topic_stats, yearly_trends, country_stats

class TrendAnalysisAgent:
    def __init__(self):
        self.name = "📈 Trend Analysis Agent"
        self.status = "idle"
    
    def analyze_trends(self, papers, db):
        self.status = "working"
        time.sleep(0.3)
        
        # Growth Analysis
        growth_analysis = {}
        for topic_info in db.topics:
            topic_name = topic_info['name']
            topic_papers = papers[papers['topic'] == topic_name]
            
            if len(topic_papers) > 0:
                growth_analysis[topic_name] = {
                    'papers': len(topic_papers),
                    'trend': topic_info['trend'],
                    'growth': topic_info['growth'],
                    'avg_citations': topic_papers['citations'].mean()
                }
        
        # Hot Topics (highest growth)
        hot_topics = sorted(growth_analysis.items(), 
                          key=lambda x: x[1]['growth'], 
                          reverse=True)[:5]
        
        # Collaboration Networks
        collab_strength = papers.groupby('university')['authors'].mean().sort_values(ascending=False)
        
        self.status = "completed"
        return growth_analysis, hot_topics, collab_strength

class RecommendationAgent:
    def __init__(self):
        self.name = "💡 Recommendation Agent"
        self.status = "idle"
    
    def generate_smart_recommendations(self, top_topics, uni_stats, growth_analysis):
        self.status = "working"
        time.sleep(0.2)
        
        recommendations = {
            "research_focus": [],
            "collaboration": [],
            "emerging_areas": [],
            "strategic": []
        }
        
        # Research Focus Recommendations
        for topic in list(top_topics.head(3).index):
            if topic in growth_analysis:
                trend = growth_analysis[topic]['trend']
                recommendations["research_focus"].append(
                    f"Focus on **{topic}** {trend} - High impact area with {growth_analysis[topic]['growth']}% growth"
                )
        
        # Collaboration Recommendations
        top_unis = uni_stats.head(3).index.tolist()
        recommendations["collaboration"].append(
            f"Consider partnerships with: **{', '.join(top_unis)}** - Leading research output"
        )
        
        # Emerging Areas
        hot_topics = [k for k, v in growth_analysis.items() if v['growth'] > 30]
        if hot_topics:
            recommendations["emerging_areas"].append(
                f"Emerging opportunities: **{', '.join(hot_topics[:3])}**"
            )
        
        # Strategic Recommendations
        recommendations["strategic"].append(
            "Increase industry-academia collaboration for real-world AI applications"
        )
        recommendations["strategic"].append(
            "Invest in AI Ethics and Responsible AI research (currently underrepresented)"
        )
        
        self.status = "completed"
        return recommendations

class ReportingAgent:
    def __init__(self):
        self.name = "📝 Report Generation Agent"
        self.status = "idle"
    
    def create_visualizations(self, uni_stats, topic_stats, yearly_trends, country_stats):
        self.status = "working"
        time.sleep(0.3)
        
        visualizations = {}
        
        # University Rankings
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(
            x=uni_stats.index[:8],
            y=uni_stats['paper_count'][:8],
            name='Papers',
            marker_color='lightblue'
        ))
        fig1.add_trace(go.Scatter(
            x=uni_stats.index[:8],
            y=uni_stats['avg_citations'][:8],
            name='Avg Citations',
            yaxis='y2',
            marker_color='red',
            mode='lines+markers'
        ))
        fig1.update_layout(
            title='Top Universities: Papers vs Average Citations',
            yaxis=dict(title='Number of Papers'),
            yaxis2=dict(title='Avg Citations', overlaying='y', side='right'),
            hovermode='x unified',
            height=400
        )
        visualizations['universities'] = fig1
        
        # Topic Distribution
        fig2 = px.pie(
            values=topic_stats['paper_count'],
            names=topic_stats.index,
            title='Research Distribution by Topic',
            hole=0.4,
            height=400
        )
        visualizations['topics_pie'] = fig2
        
        # Topic Citations
        fig3 = px.bar(
            x=topic_stats.index[:8],
            y=topic_stats['total_citations'][:8],
            color=topic_stats['total_citations'][:8],
            labels={'x': 'Topic', 'y': 'Total Citations'},
            title='Top Topics by Total Citations',
            color_continuous_scale='Viridis',
            height=400
        )
        visualizations['topics_bar'] = fig3
        
        # Yearly Trends
        fig4 = px.line(
            yearly_trends,
            x='year',
            y='count',
            color='topic',
            markers=True,
            title='Research Trends Over Time',
            labels={'count': 'Number of Papers', 'year': 'Year'},
            height=400
        )
        visualizations['trends'] = fig4
        
        # Country Map
        fig5 = px.bar(
            x=country_stats.index,
            y=country_stats['paper_count'],
            color=country_stats['total_citations'],
            labels={'x': 'Country', 'y': 'Papers', 'color': 'Citations'},
            title='Research Output by Country',
            color_continuous_scale='Blues',
            height=400
        )
        visualizations['countries'] = fig5
        
        self.status = "completed"
        return visualizations
    
    def generate_report(self, papers, uni_stats, topic_stats, recommendations, growth_analysis):
        report = f"""
# 🎓 AI Research Trends Analysis Report
## MENA Universities Research Output

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## Executive Summary

This comprehensive analysis covers **{len(papers)}** research papers from leading MENA universities,
representing cutting-edge AI research across the region.

### Key Metrics
- **Total Citations:** {papers['citations'].sum():,}
- **Average Citations per Paper:** {papers['citations'].mean():.1f}
- **Universities Analyzed:** {papers['university'].nunique()}
- **Research Topics:** {papers['topic'].nunique()}
- **Countries Represented:** {papers['country'].nunique()}

---

## 🏆 Top Universities by Research Output

"""
        for idx, (uni, row) in enumerate(uni_stats.head(5).iterrows(), 1):
            medal = "🥇" if idx == 1 else "🥈" if idx == 2 else "🥉" if idx == 3 else f"{idx}."
            report += f"{medal} **{uni}**\n"
            report += f"   - Papers: {int(row['paper_count'])}\n"
            report += f"   - Total Citations: {int(row['total_citations'])}\n"
            report += f"   - Average Citations: {row['avg_citations']:.1f}\n"
            report += f"   - H-Index Contribution: {int(row['h_index'])}\n\n"
        
        report += "\n---\n\n## 📊 Top Research Topics\n\n"
        
        for idx, (topic, row) in enumerate(topic_stats.head(8).iterrows(), 1):
            trend = "↑↑↑" if topic in ["Generative AI", "AI Ethics"] else "↑↑" if topic in ["NLP", "Edge AI"] else "↑"
            report += f"{idx}. **{topic}** {trend}\n"
            report += f"   - Papers: {int(row['paper_count'])}\n"
            report += f"   - Total Citations: {int(row['total_citations'])}\n"
            report += f"   - Avg Citations: {row['avg_citations']:.1f}\n\n"
        
        report += "\n---\n\n## 🔥 Hot Topics & Emerging Trends\n\n"
        
        hot = sorted(growth_analysis.items(), key=lambda x: x[1]['growth'], reverse=True)[:5]
        for topic, data in hot:
            report += f"### {topic} {data['trend']}\n"
            report += f"- Growth Rate: **{data['growth']}%**\n"
            report += f"- Papers: {data['papers']}\n"
            report += f"- Avg Citations: {data['avg_citations']:.1f}\n\n"
        
        report += "\n---\n\n## 💡 Strategic Recommendations\n\n"
        
        report += "### Research Focus\n"
        for rec in recommendations['research_focus']:
            report += f"- {rec}\n"
        
        report += "\n### Collaboration Opportunities\n"
        for rec in recommendations['collaboration']:
            report += f"- {rec}\n"
        
        report += "\n### Emerging Areas\n"
        for rec in recommendations['emerging_areas']:
            report += f"- {rec}\n"
        
        report += "\n### Strategic Actions\n"
        for rec in recommendations['strategic']:
            report += f"- {rec}\n"
        
        report += "\n---\n\n## 📅 Timeline & Future Outlook\n\n"
        report += "The MENA region is experiencing rapid growth in AI research:\n\n"
        report += "- **2022-2023:** Foundation building in core AI topics\n"
        report += "- **2024:** Explosive growth in Generative AI and AI Ethics\n"
        report += "- **Future:** Expected expansion in Edge AI, XAI, and Industry Applications\n"
        
        report += f"\n---\n\n*Report generated by Multi-Agent Analysis System*\n"
        report += f"*Data Source: {len(papers)} research papers from MENA universities*"
        
        return report

# -----------------------------
# Enhanced Streamlit UI
# -----------------------------
st.set_page_config(page_title="AI Research Trends - MENA", page_icon="🎓", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 1rem;
    }
    .agent-card {
        background: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">🎓 AI Research Trends in MENA Universities</p>', unsafe_allow_html=True)
st.markdown("### Advanced Multi-Agent Analysis System")

# Initialize
db = ResearchDatabase()
search_agent = SearchAgent()
analysis_agent = AnalysisAgent()
trend_agent = TrendAnalysisAgent()
rec_agent = RecommendationAgent()
report_agent = ReportingAgent()

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    
    uni_names = [u['name'] for u in db.universities]
    topic_names = [t['name'] for t in db.topics]
    
    selected_unis = st.multiselect("🏛️ Select Universities", uni_names, default=uni_names[:5])
    selected_topics = st.multiselect("🎯 Select Topics", topic_names, default=topic_names[:6])
    year_range = st.slider("📅 Year Range", 2022, 2024, (2022, 2024))
    min_citations = st.number_input("📈 Minimum Citations", 0, 100, 0, step=5)
    
    st.markdown("---")
    
    show_advanced = st.checkbox("🔬 Show Advanced Analytics", value=True)
    show_visualizations = st.checkbox("📊 Show All Visualizations", value=True)
    
    st.markdown("---")
    
    run_btn = st.button("🚀 Run Multi-Agent Analysis", type="primary", use_container_width=True)
    
    st.markdown("---")
    st.info("💡 **Tip:** Select multiple universities and topics for comprehensive analysis")

# Main Content
if run_btn and selected_unis and selected_topics:
    
    # Agent Status Dashboard
    st.subheader("🤖 Agent Activity Monitor")
    
    agent_cols = st.columns(5)
    status_containers = []
    
    for idx, agent in enumerate([search_agent, analysis_agent, trend_agent, rec_agent, report_agent]):
        with agent_cols[idx]:
            status_containers.append(st.empty())
            status_containers[idx].markdown(f"**{agent.name}**\n\n⏳ Idle")
    
    # Progress Bar
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Agent 1: Search
    status_containers[0].markdown(f"**{search_agent.name}**\n\n🔄 Working...")
    progress_bar.progress(20)
    filtered_papers, search_stats = search_agent.filter_papers(
        db, selected_unis, selected_topics, year_range, min_citations
    )
    status_containers[0].markdown(f"**{search_agent.name}**\n\n✅ Completed")
    
    # Agent 2: Analysis
    status_containers[1].markdown(f"**{analysis_agent.name}**\n\n🔄 Working...")
    progress_bar.progress(40)
    uni_stats, topic_stats, yearly_trends, country_stats = analysis_agent.compute_advanced_stats(filtered_papers)
    status_containers[1].markdown(f"**{analysis_agent.name}**\n\n✅ Completed")
    
    # Agent 3: Trends
    status_containers[2].markdown(f"**{trend_agent.name}**\n\n🔄 Working...")
    progress_bar.progress(60)
    growth_analysis, hot_topics, collab_strength = trend_agent.analyze_trends(filtered_papers, db)
    status_containers[2].markdown(f"**{trend_agent.name}**\n\n✅ Completed")
    
    # Agent 4: Recommendations
    status_containers[3].markdown(f"**{rec_agent.name}**\n\n🔄 Working...")
    progress_bar.progress(80)
    recommendations = rec_agent.generate_smart_recommendations(topic_stats['total_citations'], uni_stats, growth_analysis)
    status_containers[3].markdown(f"**{rec_agent.name}**\n\n✅ Completed")
    
    # Agent 5: Reporting
    status_containers[4].markdown(f"**{report_agent.name}**\n\n🔄 Working...")
    progress_bar.progress(90)
    visualizations = report_agent.create_visualizations(uni_stats, topic_stats, yearly_trends, country_stats)
    final_report = report_agent.generate_report(filtered_papers, uni_stats, topic_stats, recommendations, growth_analysis)
    status_containers[4].markdown(f"**{report_agent.name}**\n\n✅ Completed")
    
    progress_bar.progress(100)
    time.sleep(0.3)
    progress_bar.empty()
    
    st.success("✅ All agents completed successfully!")
    st.balloons()
    
    # Results Section
    st.markdown("---")
    st.header("📊 Analysis Results")
    
    # Key Metrics
    metric_cols = st.columns(5)
    metric_cols[0].metric("Papers Found", search_stats['papers_found'], "📄")
    metric_cols[1].metric("Total Citations", f"{search_stats['total_citations']:,}", "📈")
    metric_cols[2].metric("Avg Citations", f"{search_stats['avg_citations']:.1f}", "⭐")
    metric_cols[3].metric("Universities", len(selected_unis), "🏛️")
    metric_cols[4].metric("Topics", len(selected_topics), "🎯")
    
    # Tabs for different views
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Overview", "🏆 Rankings", "🔥 Hot Topics", "💡 Recommendations", "📄 Full Report"
    ])
    
    with tab1:
        st.subheader("Research Overview")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.plotly_chart(visualizations['universities'], use_container_width=True)
            st.plotly_chart(visualizations['topics_pie'], use_container_width=True)
        
        with col2:
            st.plotly_chart(visualizations['topics_bar'], use_container_width=True)
            st.plotly_chart(visualizations['countries'], use_container_width=True)
        
        if show_visualizations:
            st.plotly_chart(visualizations['trends'], use_container_width=True)
    
    with tab2:
        st.subheader("🏆 University Rankings")
        
        st.dataframe(
            uni_stats.style.background_gradient(subset=['total_citations', 'paper_count'], cmap='YlGn')
                         .format({'avg_citations': '{:.1f}', 'h_index': '{:.0f}'}),
            use_container_width=True,
            height=400
        )
        
        st.subheader("📊 Topic Rankings")
        st.dataframe(
            topic_stats.style.background_gradient(subset=['total_citations'], cmap='Blues')
                           .format({'avg_citations': '{:.1f}'}),
            use_container_width=True,
            height=400
        )
    
    with tab3:
        st.subheader("🔥 Hottest Research Topics")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            for idx, (topic, data) in enumerate(hot_topics, 1):
                with st.container():
                    st.markdown(f"### {idx}. {topic} {data['trend']}")
                    
                    metric_col1, metric_col2, metric_col3 = st.columns(3)
                    metric_col1.metric("Growth", f"{data['growth']}%")
                    metric_col2.metric("Papers", data['papers'])
                    metric_col3.metric("Avg Citations", f"{data['avg_citations']:.1f}")
                    
                    st.progress(min(data['growth'] / 100, 1.0))
                    st.markdown("---")
        
        with col2:
            st.markdown("### 📈 Growth Indicators")
            st.markdown("**Legend:**")
            st.markdown("- ↑↑↑ Explosive (>50%)")
            st.markdown("- ↑↑ High (25-50%)")
            st.markdown("- ↑ Moderate (10-25%)")
            st.markdown("- → Stable (<10%)")
            
            st.markdown("---")
            st.markdown("### 🎯 Quick Insights")
            st.info(f"**Fastest Growing:** {hot_topics[0][0]}")
            st.success(f"**Most Papers:** {topic_stats['paper_count'].idxmax()}")
            st.warning(f"**Highest Citations:** {topic_stats['total_citations'].idxmax()}")
    
    with tab4:
        st.subheader("💡 Strategic Recommendations")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🎯 Research Focus")
            for rec in recommendations['research_focus']:
                st.success(rec)
            
            st.markdown("### 🌟 Emerging Areas")
            for rec in recommendations['emerging_areas']:
                st.info(rec)
        
        with col2:
            st.markdown("### 🤝 Collaboration")
            for rec in recommendations['collaboration']:
                st.warning(rec)
            
            st.markdown("### 📋 Strategic Actions")
            for rec in recommendations['strategic']:
                st.error(rec)
    
    with tab5:
        st.subheader("📄 Comprehensive Report")
        
        st.markdown(final_report)
        
        # Download buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.download_button(
                "📥 Download Report (TXT)",
                data=final_report,
                file_name=f"AI_Research_Report_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
                mime="text/plain",
                use_container_width=True
            )
        
        with col2:
            csv_data = filtered_papers.to_csv(index=False)
            st.download_button(
                "📊 Download Data (CSV)",
                data=csv_data,
                file_name=f"research_data_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                use_container_width=True
            )
        
        with col3:
            stats_data = uni_stats.to_csv()
            st.download_button(
                "📈 Download Statistics",
                data=stats_data,
                file_name=f"university_stats_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                use_container_width=True
            )

else:
    # Welcome Screen
    st.info("👈 **Configure your analysis parameters in the sidebar and click 'Run Multi-Agent Analysis'**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🔍 Agent 1: Search")
        st.markdown("""
        - Filters 500+ papers
        - Multi-criteria selection
        - Real-time statistics
        """)
    
    with col2:
        st.markdown("### 📊 Agent 2: Analysis")
        st.markdown("""
        - Advanced metrics
        - Trend detection
        - Statistical modeling
        """)
    
    with col3:
        st.markdown("### 💡 Agent 3: Insights")
        st.markdown("""
        - Smart recommendations
        - Strategic planning
        - Future predictions
        """)
    
    st.markdown("---")
    
    # Sample Data Preview
    st.subheader("📊 Sample Dataset Preview")
    st.dataframe(db.papers.head(10), use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🎓 AI Research Trends Analyzer | Enhanced Multi-Agent System</p>
    <p>🚀 100% Free | No APIs | Pure Python | Advanced Analytics</p>
</div>
""", unsafe_allow_html=True)