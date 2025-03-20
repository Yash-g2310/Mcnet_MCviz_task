import pylhe
import json
from flask import Flask, jsonify

def convert_to_json(file_path):
    lhe = pylhe.read_lhe_file(file_path)
    dict = {}
    dict["init_info"] = lhe.init["initInfo"]
    
    events = list(lhe.events)
    dict["num_events"] = len(events)
    dict["events"] = []
    
    for i, event in enumerate(events):
        eventInfo = event.eventinfo
        
        particles = list(event.particles)
        final_particles = [p for p in particles if p.status == 1]
        initial_particles = [p for p in particles if p.status == -1]
        intermediate_particles = [p for p in particles if p.status == 2]
                
        sum_px = sum(p.px for p in particles)
        sum_py = sum(p.py for p in particles)
        sum_pz = sum(p.pz for p in particles)
        sum_E  = sum(p.e for p in particles)
        
        event_dict = {}
        event_dict["event_number"] = i + 1
        event_dict["total_particles"] = eventInfo.nparticles
        event_dict["initial_particles"] = len(initial_particles)
        event_dict["final_particles"] = len(final_particles)
        event_dict["intermediate_particles"] = len(intermediate_particles)
        event_dict["momentum_sums"] = {
            "px": sum_px,
            "py": sum_py,
            "pz": sum_pz
        }
        event_dict["total_energy"] = sum_E
        event_dict["process_id"] = eventInfo.pid
        event_dict["event_weight"] = eventInfo.weight
        event_dict["energy_scale"] = eventInfo.scale
        event_dict["electromagnetic_coupling"] = eventInfo.aqed
        event_dict["strong_coupling"] = eventInfo.aqcd
        
        event_dict["particles"] = []
        for particle in event.particles:
            particle_dict = {
                "id": particle.id,
                "status": particle.status,
                "mother1": particle.mother1,
                "mother2": particle.mother2,
                "color1": particle.color1,
                "color2": particle.color2,
                "px": particle.px,
                "py": particle.py,
                "pz": particle.pz,
                "e": particle.e,
                "m": particle.m
            }
            event_dict["particles"].append(particle_dict)
        dict["events"].append(event_dict)
    
    output_file = './output/event_info_json.json'
    with open(output_file, 'w') as f:
        json.dump(dict, f, indent=4)
    
    return dict

formatted_events = convert_to_json('top.lhe')

app = Flask(__name__)

@app.route('/event/<int:id>', methods=['GET'])
def get_event(id):
    id = int(id)
    if 0 < id <= len(formatted_events["events"]):
        event = formatted_events["events"][id - 1]
        return jsonify(event)
    else:
        return jsonify({"error": "Event not found"}), 404

@app.route('/', methods=['GET'])
def get_events_details():
    message = {
        "message": "Individual information for each event is available at /event/<id>",
        "events": {
            "init_info": formatted_events["init_info"],
            "num_events": formatted_events["num_events"]
        }
    }
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)