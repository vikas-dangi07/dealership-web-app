(async function(){
 const list=document.getElementById("dealer-list");
 if(!list)return;
 const filter=document.getElementById("state-filter");
 async function load(){
  list.innerHTML="<p>Loading dealerships…</p>";
  const state=filter.value;
  const url=state?`/djangoapp/get_dealers/${encodeURIComponent(state)}/`:"/djangoapp/get_dealers/";
  try{
   const response=await fetch(url); const data=await response.json();
   const dealers=data.dealers||[];
   if(!dealers.length){list.innerHTML="<p>No dealerships found for this selection.</p>";return;}
   list.innerHTML=dealers.map(d=>`<article class="dealer-card"><p class="eyebrow">DEALERSHIP</p><h3>${escapeHtml(d.full_name)}</h3><p class="meta">${escapeHtml(d.city)}, ${escapeHtml(d.state)}</p><p>${escapeHtml(d.address||"Address not provided")}</p><p>${escapeHtml(d.phone||"")}</p><a href="/djangoapp/get_dealer_details/${d.id}/" target="_blank" rel="noopener">View dealer details & reviews →</a></article>`).join("");
  }catch(e){list.innerHTML="<p>Could not load dealers. Run migrations and seed demo data, then refresh.</p>";}
 }
 function escapeHtml(s){return String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));}
 filter?.addEventListener("change",load); load();
})();
