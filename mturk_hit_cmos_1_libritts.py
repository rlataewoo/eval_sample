
def generate_classifier_block(sample_num, transcript):
    sample_id = f"sample_{sample_num:03d}"
    audio_a_url = f"https://rlataewoo.github.io/eval_sample/samples/table_2/libritts_mp3/{sample_id}_A.mp3?raw=true"
    audio_b_url = f"https://rlataewoo.github.io/eval_sample/samples/table_2/libritts_mp3/{sample_id}_B.mp3?raw=true"
    audio_ref_url = f"https://rlataewoo.github.io/eval_sample/samples/table_2/libritts_mp3/{sample_id}_Ref.mp3?raw=true"

    return f"""
    <crowd-classifier 
        categories="['-3 Reference Much Better', '-2 Reference Better', '-1 Reference Little Better' ,'0 Equally Natural', '+1 Sample Little Better', '+2 Sample Better', '+3 Sample Much Better']"
        header="How natural does the audio sound compared to the reference? Please focus on whether the transition between the original and synthesized parts is smooth and human-like."
        name="{sample_id}-naturalness">
            <classification-target>               
                <div style="margin-bottom: 20px;">
                <label>Reference audio</label>
                <audio controls style="width: 100%">
                    <source src="{audio_ref_url}" type="audio/mp3" />
                </audio>
                </div>
         
                <div style="margin-bottom: 20px;">
                <label>Sample audio</label>
                <audio controls style="width: 100%">
                    <source src="{audio_a_url}" type="audio/mp3" />
                </audio>
                </div>
                
                <div class="sample-number" style="margin-top: 10px; margin-bottom: 10px; font-weight: bold; font-size: 30px;">Sample {sample_num:03d}-A</div>
                <div id="text_area">
                    <h3>Transcripts (edited parts are shown in <span style='color: red;'>red</span>)</h3>
                    <p>{transcript}</p>
                </div>
            </classification-target>
        <short-instructions>  
            <p>
              Listen to the sample of computer generated speech and assess the quality 
              of the audio based on how close it is to natural speech. The words in the audio are shown in the Original utterance below.
            </p>
            For better results, wear headphones and work in a quiet environment.
            If the audio file is not playing, please be patient as it may take some time for the audio file to upload.
        </short-instructions>
    </crowd-classifier>

    <crowd-classifier 
        categories="['-3 Reference Much Better', '-2 Reference Better', '-1 Reference Little Better' ,'0 Equally Natural', '+1 Sample Little Better', '+2 Sample Better', '+3 Sample Much Better']"
        header="How natural does the audio sound compared to the reference? Please focus on whether the transition between the original and synthesized parts is smooth and human-like."
        name="{sample_id}-naturalness">
            <classification-target>               
                <div style="margin-bottom: 20px;">
                <label>Reference audio</label>
                <audio controls style="width: 100%">
                    <source src="{audio_ref_url}" type="audio/mp3" />
                </audio>
                </div>
         
                <div style="margin-bottom: 20px;">
                <label>Sample audio</label>
                <audio controls style="width: 100%">
                    <source src="{audio_b_url}" type="audio/mp3" />
                </audio>
                </div>
                
                <div class="sample-number" style="margin-top: 10px; margin-bottom: 10px; font-weight: bold; font-size: 30px;">Sample {sample_num:03d}-B</div>
                <div id="text_area">
                    <h3>Transcripts (edited parts are shown in <span style='color: red;'>red</span>)</h3>
                    <p>{transcript}</p>
                </div>
            </classification-target>
        <short-instructions>  
            <p>
              Listen to the sample of computer generated speech and assess the quality 
              of the audio based on how close it is to natural speech. The words in the audio are shown in the Original utterance below.
            </p>
            For better results, wear headphones and work in a quiet environment.
            If the audio file is not playing, please be patient as it may take some time for the audio file to upload.
        </short-instructions>
    </crowd-classifier>

    """

def generate_hit_file(filename, start_idx, end_idx, transcript_map):
    html_blocks = ['<!-- You must include this JavaScript file -->',
                   '<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>',
                   '<crowd-form answer-format="flatten-objects">']
    
    for i in range(start_idx, end_idx + 1):
        transcript = transcript_map[i]
        html_blocks.append(generate_classifier_block(i, transcript))

    html_blocks.append('</crowd-form>')

    full_html = '\n'.join(html_blocks)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(full_html)



# 각 샘플 번호와 대응하는 텍스트
transcript_map = {
    1: "You see loving <span style='color: red;'>some one as I love you</span> makes the whole world different.",
    2: "At any rate my <span style='color: red;'>eloquence was altogether stopped. The gentleman</span> was named Sir Ferdinando Brown.",
    3: "Mary your father and I are going out <span style='color: red;'>to ride this afternoon and I am sorry for your</span> sake that we can not take you with us.",
    4: "Whoever therefore is ambitious <span style='color: red;'>of distinction in this way ought</span> to be prepared for disappointment.",
    5: "I wonder though if people <span style='color: red;'>could see the light from the street</span> through any chinks in the boarding?",
    6: "The Abraham Lincoln <span style='color: red;'>had been perfectly chosen and fitted</span> out for its new assignment.",
    7: "Ten days were consumed <span style='color: red;'>in these negotiations; but the spirit</span> of vengeance refused to yield.",
    8: "The wheat cutting sometimes goes on all night <span style='color: red;'>as well as all day and in good seasons there</span> are scarcely men and horses enough to do the harvesting.",
    9: "I have very few to love <span style='color: red;'>me now and I thought you might love</span> me as I have begun to love you.",
    10: "My dear Sir I <span style='color: red;'>should reply (or Madam) you have</span> come to the right shop.",

    11: "'We indeed!' cried the <span style='color: red;'>Mouse who was trembling down to</span> the end of his tail.",
    12: "Surely some portion <span style='color: red;'>of the Casbah must still</span> rise above the waves?",
    13: "As for ourselves we shall soon <span style='color: red;'>reach some retired spot where no eyes can</span> see us and no step follow ours.",
    14: "The first person he met <span style='color: red;'>was a farm labourer walking alongside a load</span> of peat and smacking at his horse.",
    15: "That is <span style='color: red;'>all quite true Mr Neverbend</span> said Sir Ferdinando Brown.",
    16: "The first page on the <span style='color: red;'>floor the second in the window the</span> third where you left it said he.",
    17: "As they led the <span style='color: red;'>now famous animal from the room</span> the Boolooroo shuddered and said:",
    18: "I remained there alone for many hours but I <span style='color: red;'>must acknowledge that before I left the chambers I had gradually</span> brought myself to look at the matter in another light.",
    19: "The etiquette is to have <span style='color: red;'>two bites before the butler and the</span> three footmen whisk away the plate.",
    20: "But the affair was magnified <span style='color: red;'>as a crowning proof that the free</span> State men were insurrectionists and outlaws.",

    21: "But it is not with a <span style='color: red;'>view to distinction that you should cultivate this</span> talent if you consult your own happiness.",
    22: "First bind the Earth Man in the <span style='color: red;'>frame commanded the Boolooroo. We'll slice him in two</span> before we do the same to the billygoat.",
    23: "Can you give me a few <span style='color: red;'>hints? --suppose you spoke to me like this</span> then I could do something for you.",
    24: "During and after the contest <span style='color: red;'>over the speakership at Washington each State</span> Legislature became a forum of Kansas debate.",
    25: "This trading votes <span style='color: red;'>which was often done was considered</span> by the politicians quite legitimate.",
    26: "Sheriff Jones made several visits unmolested on <span style='color: red;'>their part and without any display of writs or demand</span> for the surrender of alleged offenders on his own.",
    27: "It seems to <span style='color: red;'>be easier than it is I</span> begin to think replied Philip.",
    28: "All were agreed that one could be <span style='color: red;'>ordered but that it was not a usual size of</span> pencil and that it was seldom kept in stock.",
    29: "Hold him steady <span style='color: red;'>in the frame and I'll</span> tie him up she replied.",
    30: "Oh she said he has such <span style='color: red;'>an extraordinarily fine cap on his head that that</span> will do just as well as a uniform.",

    31: "Yes indeed those are the marks <span style='color: red;'>of teeth imprinted upon the metal! The jaws which</span> they arm must be possessed of amazing strength.",
    32: "It went into service <span style='color: red;'>august fifteenth eighteen eighty two about three</span> weeks before the Pearl Street station.",
    33: "The master and mistress begged them not <span style='color: red;'>to cry or raise their voices in lamentation; for</span> it would do the little patient no good.",
    34: "Yes yes she hurried pulling <span style='color: red;'>her hand gently away from him. Presently</span> it stole back to his coat sleeve.",
    35: "I want to be <span style='color: red;'>something to make myself something</span> to do something.",
    36: "Then dear said mrs Whitney you must be kinder <span style='color: red;'>to her than ever; think what it would be for one</span> of you to be away from home even among friends.",
    37: "One day when the boy was sent by his <span style='color: red;'>grandfather with a message to a relation he passed along a</span> street in which there was a great concourse of horsemen.",
    38: "I had however promised to <span style='color: red;'>take tea in a friend's rooms so</span> I left the proof upon my desk.",
    39: "Fairview was twelve miles <span style='color: red;'>away but by ten o'clock they</span> drew up at the county jail.",
    40: "Don't mind him <span style='color: red;'>Cap'n said Trot but fetch</span> him along to the frame.",
}
generate_hit_file("hit_cmos_1_libritts.html", 1, 40, transcript_map)
